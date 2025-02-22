from datetime import datetime
import helper

class request_response:
    def __init__(self,symbol:str, start_date:datetime=None, end_date:datetime=None) -> None:
        self.symbol:str = symbol
        self.update(start_date, end_date)
        self.data:dict = {}

    def update(self, start_date:datetime, end_date:datetime) -> None:
        self.start_date:datetime = start_date
        self.end_date:datetime = end_date
        self.start_period:int = helper.dt.to_timestamp(start_date)
        self.end_period:int = helper.dt.to_timestamp(end_date)
        

    def clear(self) -> None:
        self.symbol = None
        self.start_date = None
        self.end_date = None
        self.start_period = None
        self.end_period = None