from logging import INFO
import sqlite3
from enum import Enum
from datetime import datetime as dt;
from Logging import OutputLogger
from Logging.OutputLogger import LogLevel

class Data_Type(Enum):
    NULL = "The value is a NULL value"
    INTEGER = "The value is a signed integer, stored in 0, 1, 2, 3, 4, 6, or 8 bytes depending on the magnitude of the value."
    REAL = "The value is a floating point value, stored as an 8-byte IEEE floating point number."
    TEXT = "The value is a text string, stored using the database encoding (UTF-8, UTF-16BE or UTF-16LE)."
    BLOB = "The value is a blob of data, stored exactly as it was input."

# Using __enter__ and __exit__ allows me to use "with" to manage my connection to the database
class SQLiteDatabaseConnector:
    _database_name: str
    _connection: sqlite3.Connection
    
    # Class gets initialised with the database name
    def __init__(self, database_name):
        self._database_name = database_name      
     
    #__enter__ method acquires the resource and returns it.
    def __enter__(self):
        try:
            self._connection = sqlite3.connect(self._database_name)
            OutputLogger.log(f"Connection was established to: {self._database_name}", LogLevel.INFO)#TODO
            return self
        except sqlite3.Error as e:
            OutputLogger.log_error(f"Error connecting to database: {e}")
     
    # __exit__ method releases the resource and handles cleanup
    def __exit__(self, exc_type, exc_value, traceback):
        if self._connection:
            self._connection.close()
            OutputLogger.log(f"Disconnected from database: {self._database_name}")
            
    def fetch_all(self, table_name) -> tuple[list, bool]:
        '''
        Gets all data from the table
        retuns list of rows AND bool to indicate if fetch was successful
        '''
        try:
            cursor = self._connection.cursor()
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()
            return rows, True
        except sqlite3.Error as e:
            OutputLogger.log_error(f"Error fetching data from table: {e}")
            return [], False
        
    def execute_sql(self, sql, params=None):
        try:
            cursor = self._connection.cursor()
            if params:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)
            self._connection.commit()
            return(cursor.fetchall())
        except sqlite3.Error as e:
            OutputLogger.log_error(f"{dt.now()} :Error executing SQL statement: {e}")
            
    def create_table(self, table_name: str, structure: dict, primary_key:str = "_ID" ):
        execure_sql: str = f"CREATE TABLE {table_name} ("
        for field_name, field_type in structure.items():
            execure_sql += f"{field_name} {field_type.name},"
        execure_sql += f"{primary_key} {Data_Type.INTEGER.name} PRIMARY KEY);"  
        self.execute_sql(execure_sql)