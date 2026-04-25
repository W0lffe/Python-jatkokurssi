import sqlite3 as sql

db_file='my_db.db'

mydb = sql.connect(db_file)


create_table_query = """
CREATE TABLE IF NOT EXISTS texttable (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
"""
create_insert_query = """
INSERT INTO texttable (name)
VALUES ('Matti'), ('Ville'), ('Kaisa'), ('Mikko');
"""

cursor = mydb.cursor()
cursor.execute(create_table_query)
cursor.execute(create_insert_query)

mydb.commit()
cursor.close()
mydb.close()

