from tkinter import *
import sqlite3 as sql
db_file='my_db.db'

#Your code here!
mydb = sql.connect(db_file)
cursor = mydb.cursor()

select_query = """
    SELECT data FROM textdata;
"""
cursor.execute(select_query)
fetchedData = cursor.fetchall()
data = [row[0] for row in fetchedData]

index = 0

def on_button_click():
    global index

    if len(data) == 0:
        lbl.config(text="")
        return

    lbl.config(text=data[index])
    index = (index + 1) % len(data)



root = Tk()

lbl = Label(root, text="")
lbl.pack()

btn = Button(root, text="Next", command=on_button_click)
btn.pack()


#Don't modify lines below
if __name__ == "__main__":
    root.mainloop()
