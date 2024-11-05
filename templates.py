from datetime import datetime
from declared_enums import ScrapeMethod
from database import DataBase
from webscraper import request_response


class WebScraper:
    def __init__(self,database:DataBase):
        """Initialise response class, database and user agent to be used, response object will holds the data returned from the get request and written to the
        appropriate database table, response objest will be reused for subsequent calls"""
        self.db:DataBase = database
        self.response_info:request_response = request_response()
        self.user_agent={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:129.0) Gecko/20100101 Firefox/129.0'}

    def __call__(self, method:ScrapeMethod, d1:datetime, d2:datetime) -> None:
        """Decides which method to use
        Method:
            For a given stock.
            ALL: Scrapes all data.
            FROM: Scrapes all data from data specified to present day.
            TO: Scrapes all data from first record to data specified.
            FROMTO: Scrapes all data from first date specified to second date specified.
        """
    def scrape(self) -> None:
        """Will repeatedly use the get, transform and write members to sequentially scrape and write data to database"""
        pass 
        

    def get(self) -> None:
        """This function will use the request object to make the get request,
        and store the response as a dictionary within the response object"""
        pass
        

    def transform(self) -> bool:
        """Transformation steps for the response object will be executed returning true if response object is valid"""
        
        return True


    def write(self):
        """Writes response object to database"""
        pass
            