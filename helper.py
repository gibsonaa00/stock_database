# Packages
from datetime import datetime,timedelta
from typing import Callable
from enum import Enum
import calendar
# Custom
from features import Columns


class dt:
    @staticmethod
    def freq_map():
        return {"d":1,"m":30,"y":365}
    # Helper Functions
    @staticmethod
    def get_date_n_ago(date:datetime, period:int, freq:str="d") -> str:
        return date-timedelta(days=period*dt.freq_map()[freq])
            

    @staticmethod
    def get_today_date() -> str:
        return datetime.today()

    
    @staticmethod
    def to_timestamp(date:datetime) -> int:
        if date:
            return round(datetime.timestamp(date))
        else:
            return None

    @staticmethod
    def to_datetime_s(timestamp:int) -> int:
        return datetime.fromtimestamp(timestamp)

    @staticmethod
    def to_datetime(timestamps:list) -> int:
        to_datetime = lambda x: datetime.fromtimestamp(x)
        return [*map(to_datetime,timestamps)]

    @staticmethod
    def get_sequence(start_date:datetime, end_date:datetime, period:int, freq:str="d") -> list:
        
        seq:list = []
        while start_date < end_date:
            seq.append(start_date)
            start_date+=timedelta(days=period*helper_datetime.freq_map()[freq])
        #if seq[-1] > end_date:
        #    seq[-1] = end_date
        #elif seq[-1] != end_date:
        #    seq.append(end_date)
    
        return seq
    
    @staticmethod
    def get_last_weekday(date:datetime) -> datetime:
        yyyy_mm_dd = date.date()
        """Returns friday's date if weekend else returns same date"""
        week_day = calendar.weekday(*map(int,str(date.date()).split("-")))
        if week_day == calendar.SATURDAY:
            return yyyy_mm_dd - timedelta(days=1)
        elif week_day == calendar.SUNDAY:
            return yyyy_mm_dd - timedelta(days=2)
        else:
            return yyyy_mm_dd

    @staticmethod
    def get_month_from_num(num: int) -> str:
        months = {
            1: "January",
            2: "February",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December"
        }
        return months.get(num)


class dictionary:
    @staticmethod
    def unravel(d:dict):
        r:dict={}
        def unravel_inner(d:dict):
            for k, v in d.items():
                if isinstance(v,dict):
                    unravel_inner(v)
                    
                elif isinstance(v,list):
                    for obj in v:
                        if isinstance(obj,dict):
                            unravel_inner(obj)
                        else:
                            r[k] = v
                            
                else:
                    r[k] = v
        unravel_inner(d)
        return r

class enum:
    @staticmethod
    def to_dict(e:Enum):
        return {i.value[0]:i.value[1] for i in e}
    

class database:
    @staticmethod
    def _get_statement(get_statement:Callable):
        def wrapper(func:Callable):
            def inner(*args,statement:str=None,**kwargs) -> None:
                return func(*args,**kwargs,statement=get_statement(**kwargs))
            return inner
        return wrapper


    @staticmethod
    def _get_create_statement(table:str, columns:dict[str,str]):
        return f"CREATE TABLE IF NOT EXISTS {table} (" \
                            + ",".join([f"'{col_name}' {types}" for col_name,types in columns.items()])\
                            + ")"

    @staticmethod
    def _get_insert_statement(table:str, data:dict[str,object]):
        return (f"INSERT INTO {table} (" \
                            + ",".join([f"'{col_name}'" for col_name in data.keys()])\
                            + ") VALUES ("
                            + ",".join([f"'{val}'" for val in data.values()])\
                            + ")")


    @staticmethod
    def _get_delete_statement(table:str) -> str:
        return f"DROP TABLE IF EXISTS {table}"


    @staticmethod
    def _get_get_statement(table:str) -> str:
        return f"SELECT * FROM {table}"


    @staticmethod
    def _get_check_statement(table:str) -> str:
        return f"SELECT name FROM sqlite_master WHERE name = '{table}'"

    
    @staticmethod
    def _get_latest_date_statement(table:str) -> str:
        return f"SELECT MAX(date) AS max_date FROM {table}"

    
    @staticmethod
    def error_handle(table_check:Callable[str,bool],should_exist:bool):
        def wrapper(func):
            def inner(self,table:str):
                if table_check(table):
                    return func(self,table) if should_exist else None
                else:
                    return None if should_exist else func(self,table)
            return inner
        return wrapper


    @staticmethod
    def _log_delete(table:str):
        return f"UPDATE logs SET updated_at = '{dt.get_today_date().date()}', deleted_at = '{dt.get_today_date().date()}'  WHERE name = '{table}'; "


    @staticmethod
    def _log_create(table:str, columns:dict[str,object]):
        return f"INSERT INTO logs ('name','created_at', 'updated_at') VALUES ('{table}','{dt.get_today_date().date()}','{dt.get_today_date().date()}')"

    @staticmethod
    def _log_update(table:str):
        return f"UPDATE logs SET updated_at = '{dt.get_today_date().date()}' WHERE name = '{table}'; "

              
    @staticmethod
    def _log(log_statement:Callable):
        def wrapper(func:Callable):
            def inner(*args,**kwargs) -> None:
                args[0].Cursor.execute(log_statement(**kwargs))
                args[0].commit()    
                return func(*args,**kwargs)
            return inner
        return wrapper

    
    def dict_factory(cursor, row):
        fields = [column[0] for column in cursor.description]
        return {key: value for key, value in zip(fields, row)}

class yfinance:

    @staticmethod
    def trim_response_json(response:dict) ->dict:
        trimmed_response:dict = {}
        for pair in Columns:
            trimmed_response[pair.value[0]] = response[pair.value[0]]
        return trimmed_response
            

