import sqlite3 as sql

db_file='my_db.db'

mydb = sql.connect(db_file)

select_query = """
SELECT * FROM texttable;
"""

for row in mydb.execute(select_query):
    print(row)

mydb.close()
