import sqlite3
from sqlite3.dbapi2 import Cursor
def connect():
    db = sqlite3.connect('project1\library.db')
    cursor = db.cursor()
    cursor.row_factory = sqlite3.Row
    return cursor