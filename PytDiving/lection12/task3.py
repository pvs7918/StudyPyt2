# import sqlite3
#
# connection = sqlite3.connect('sqlite.db')
# cursor = connection.cursor()
# cursor.execute("""create table if not exists users(name, age);""")
# cursor.execute("""insert into users values ('Гвидо', 66);""")
# connection.commit()
# connection.close()


import sqlite3
class DB:
    def __init__(self, name):
        self.name = name
        self.connection = None
        self.cursor = None
    def __enter__(self):
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()
        self.cursor = self.connection = None

db = DB('sqlite.db')
with db as cur: # AttributeError: __exit__
    cur.execute("""create table if not exists users(name, age);""")
    cur.execute("""insert into users values ('Гвидо', 66);""")