import sqlite3
import helper

class DataBase(sqlite3.Connection):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.row_factory = helper.database.dict_factory
        self.Cursor = self.cursor()
        if not self.check(table="logs"):
            self.Cursor.execute(helper.database._get_create_statement(table="logs", columns={"name":"TEXT", "created_at":"TEXT","deleted_at":"TEXT", "updated_at":"TEXT"}))
            self.commit()

    @helper.database._get_statement(helper.database._get_check_statement)
    def check(self, table:str,statement:str=None) -> None:
        return True if self.Cursor.execute(statement).fetchone() else False # returns empty if not found

    @helper.database._log(helper.database._log_create)
    @helper.database._get_statement(helper.database._get_create_statement)
    def create(self, table:str, columns:dict[str,str],statement:str=None):
        self.Cursor.execute(statement)
        self.commit()

    @helper.database._log(helper.database._log_delete)
    @helper.database._get_statement(helper.database._get_delete_statement)
    def delete(self, table:str,statement:str=None) -> None:
        self.Cursor.execute(statement)
        self.commit()
          
    
    @helper.database._get_statement(helper.database._get_insert_statement)
    def insert(self, table:str,data:dict[str,object],statement:str=None) ->None:
        self.Cursor.execute(statement)
        self.commit()

    
    @helper.database._get_statement(helper.database._get_get_statement)
    def get(self, table:str,statement:str=None) ->None:
        return self.Cursor.execute(statement).fetchall()

    @helper.database._get_statement(helper.database._get_latest_date_statement)
    def get_latest_date(self, table:str,statement:str=None) -> str:
        max_date_str = self.Cursor.execute(statement).fetchall()[0]["max_date"]
        return helper.datetime.string_to_datetime(max_date_str)
        