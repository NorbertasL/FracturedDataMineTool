import sqlite3
from sqlite3 import Connection, Error

_DATABSE_PATH = "test.db"

def create_table():
    with get_db_conn(_DATABSE_PATH) as conn:
        conn = get_db_conn(_DATABSE_PATH)
        if conn is None: return False
    
        cursor = conn.cursor()
        cursor.execute("""SELECT name FROM sqlite_master  
       WHERE type='table';""")
        print(cursor.fetchall())
        #conn.close()
        print(cursor.fetchall())

def get_db_conn(db_file) -> Connection:
    """ create a database connection to a SQLite database """
    
    try:
            #print(connection.close)
        return sqlite3.connect(db_file)
            #cursor = connection.cursor()
  #           print(sqlite3.version)
  #           cursor.execute('''CREATE TABLE TestTable
  #              (Col1 text, Col2 text, Col3 real)''')
            
  #           # Save (commit) the changes
  #           connection.commit()
            
  #           cursor.execute("""SELECT name FROM sqlite_master  
  # WHERE type='table';""")
  #          print(cursor.fetchall())
            
    except Error as e:
        print(e)
    

#This block is for testing and is only executed if the script is run directly.
if __name__ == '__main__':
    create_table()
