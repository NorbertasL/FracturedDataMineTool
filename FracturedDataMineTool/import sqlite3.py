
import sqlite3
import os

_DATABASE_PATH = "test.db"


#conn = sqlite3.connect('./DatabaseFiles/'+ _DATABASE_PATH)

data_path = './DatabaseFiles/'
filename = '"test.db"'

os.makedirs(data_path, exist_ok=True)

db = sqlite3.connect(data_path + filename + '.sqlite3')
db.execute('CREATE TABLE IF NOT EXISTS TableName (id INTEGER PRIMARY KEY, quantity INTEGER)')
db.close()