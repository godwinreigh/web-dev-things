from tkinter import *
import sqlite3
root = Tk()
#databases

#create our database or connect to one
conn=sqlite3.connect('address_book2.db')
#create a cursor
c=conn.cursor()
#create table
c.execute("""CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
        )""")





#to update changes to databases
#commit changes
conn.commit()
#close connection
conn.close()

root.mainloop()