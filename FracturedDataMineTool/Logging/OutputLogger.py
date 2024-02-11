from enum import Enum
from logging import INFO
from logging.config import DEFAULT_LOGGING_CONFIG_PORT
import os
from datetime import datetime as dt;

DEFAULT_LOGGING_FILE = "log.log"

MIN_FILE_LOG_LEVEL:int = 0
MIN_CONSOLE_LOG_LEVEL:int = 0

class LogLevel(Enum): 
    DEBUG = 0,
    INFO = 1,
    WARNING = 2,
    ERROR = 3
    

def console_print(error_msg, level: LogLevel = LogLevel.DEBUG):
   print(f"{level.name}:{dt.now()} -> {error_msg}")
   
def log_error(error_msg: str, console: bool = True):
   log(error_msg, LogLevel.ERROR, console)

def log(error_msg: str, level: LogLevel = LogLevel.INFO, console: bool = True):
    try:
         # Construct full file path
        file_path = os.path.join(DEFAULT_LOGGING_FILE)
        # Write to the file
        msg: str = f"{level.name}:{dt.now()} -> {error_msg}"
        with open(file_path, 'a') as file:
            if console:
                console_print(error_msg, level)
            
            file.write(str(msg) + '\n')
                
    except Exception as e:
        console_print(f"An error occurred while writing to the file: {e}", LogLevel.ERROR)
        


 