from datetime import datetime
import requests
import helper
from declared_enums import Columns, ScrapeMethod
from database import DataBase

class request_response:
    def __init__(self,symbol:str, start_date:datetime=None, end_date:datetime=None) -> None:
        self.symbol:str = symbol
        self.update(start_date, end_date)
        self.data:dict = {}

    def update(self, start_date:datetime, end_date:datetime) -> None:
        self.start_date:datetime = start_date
        self.end_date:datetime = end_date
        self.start_period:int = helper.datetime.to_timestamp(start_date)
        self.end_period:int = helper.datetime.to_timestamp(end_date)
        

    def clear(self) -> None:
        self.symbol = None
        self.start_date = None
        self.end_date = None
        self.start_period = None
        self.end_period = None
        


class yahoo_finance:
    def __init__(self,database:DataBase, db_symbol:str):
        self.db = database
        self.db_symbol = db_symbol
        
        self.user_agent={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:129.0) Gecko/20100101 Firefox/129.0'}
        

    def __call__(self,stock:str, start_date:datetime=None, end_date:datetime=None, method:ScrapeMethod=ScrapeMethod.ALL) -> bool:
        self.method = method
        self.request_info = request_response(symbol=stock)
        self.response_info = request_response(symbol=stock)   

        
        if self.method == ScrapeMethod.ALL:
            self.start_date:datetime=helper.datetime.get_date_n_ago(helper.datetime.get_today_date(),period=40,freq="y")
            self.end_date:datetime=helper.datetime.get_today_date()
        elif self.method == ScrapeMethod.FROM:
            self.start_date:datetime=start_date
            self.end_date:datetime=helper.datetime.get_today_date()
        elif self.method == ScrapeMethod.TO:
            self.start_date:datetime=None
            self.end_date:datetime=end_date
        elif self.method == ScrapeMethod.FROMTO:
            self.start_date:datetime=start_date
            self.end_date:datetime=end_date
        else:
            raise AttributeError(f"Selected method {self.method} does not exist")

        self.scrape()
            

    def scrape(self):
        self.response_info.data["code"] = ""
        self.request_info.update(helper.datetime.get_date_n_ago(self.end_date, period=6, freq="m"), self.end_date)
        while (self._gt_start_date() and self._lt_end_date() and not self._is_bad_request()):
            self.execute()

        if self.start_date:
            self.request_info.update(self.start_date, self.request_info.end_date)
            self.execute()

    def _gt_start_date(self) -> bool:
        return self.request_info.start_date > self.start_date if self.start_date else True

    def _lt_end_date(self) -> bool:
        return self.request_info.end_date <= self.end_date if self.end_date else True

    def _is_bad_request(self) ->bool:
        return self.response_info.data.get("code").lower() == "bad request" if self.response_info.data.get("code") else False

        
    def execute(self) -> None:
        self.get()
        self.transform()
        self.write()
    

    def get(self) -> None:
        self.response_info.response = requests.get(f"https://query1.finance.yahoo.com/v8/finance/chart/{self.request_info.symbol}?formatted=true&crumb=Gg8TRsb%2F.kh&lang=en-GB&region=GB&includeAdjustedClose=true&interval=1d&period1={self.request_info.start_period}&period2={self.request_info.end_period}&events=capitalGain%7Cdiv%7Csplit&useYfid=true&corsDomain=uk.finance.yahoo.com",
                      headers=self.user_agent)
        

    def transform(self):
        self.response_info.response.string = self.response_info.response.text.replace("true","True")
        self.response_info.response.string = self.response_info.response.string.replace("false","False")
        self.response_info.response.string = self.response_info.response.string.replace("null","None")
        self.response_info.JSON = eval(self.response_info.response.string)
        self.response_info.data = helper.dictionary.unravel(self.response_info.JSON)
        if self._is_bad_request():
            return

        if not self.response_info.data.get(Columns.TIMESTAMP.value[0]):
            self.response_info.data["code"] = "bad request"
            return
        self.response_info.data[Columns.DATE.value[0]] = \
        helper.datetime.to_datetime(self.response_info.data[Columns.TIMESTAMP.value[0]])
        self.response_info.update(start_date = min(self.response_info.data[Columns.DATE.value[0]]),
                                  end_date = max(self.response_info.data[Columns.DATE.value[0]]))
        self.response_info.data = helper.yfinance.trim_response_json(self.response_info.data)

        #New request
        self.request_info.update(start_date= helper.datetime.get_date_n_ago(self.response_info.start_date,period=6, freq="m"),
                                 end_date= helper.datetime.get_date_n_ago(self.response_info.start_date,period=1,freq="d"))


    def write(self):
        if self._is_bad_request():
            return
        for idx in range(len(self.response_info.data[Columns.OPEN.value[0]])):
            self.db.insert(table=self.db_symbol, 
                      data={key:value[idx] if isinstance(value,list) else value for key, value in self.response_info.data.items()})
            

            