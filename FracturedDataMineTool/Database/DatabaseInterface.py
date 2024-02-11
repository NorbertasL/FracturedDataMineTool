
from Logging.OutputLogger import console_print
from SQLiteDatabaseConnector import Data_Type as type
from SQLiteDatabaseConnector import SQLiteDatabaseConnector as connector
from copy import deepcopy

DATABASE_PATH = "Test.db"

# using Dictionary to specify data field and types
__ITEM_TEMPLATE: dict = {
    # filed_name : field_type
    'name': type.TEXT,
    'typeID' : type.INTEGER,
    'linkingID' : type.TEXT,
    'description' : type.TEXT,
    'icon' : type.BLOB, #Still not sure if ill store it as binary
    'weight' : type.REAL,
    'maxStackCount' : type.INTEGER, 
    }


def get_item_template() -> dict[str, type]:
    return deepcopy(__ITEM_TEMPLATE)


#This block is for testing and is only executed if the script is run directly.
if __name__ == '__main__':
    #print(__ITEM_TEMPLATE_SQLite)
    
    with connector(DATABASE_PATH) as conn:
        if conn is not None:
            conn.create_table("items3", __ITEM_TEMPLATE)
            console_print(conn.execute_sql("SELECT name FROM sqlite_master WHERE type='table';"))
            