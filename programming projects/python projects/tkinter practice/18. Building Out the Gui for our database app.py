from tkinter import *
import sqlite3
root = Tk()

def submit():
    # create our database or connect to one
    conn = sqlite3.connect('address_book.db')
    # create a cursor
    c = conn.cursor()
    # databases
    #create table
    c.execute("INSERT INTO addresses VALUES(:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': adress.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
              })
    # to update changes to databases
    # commit changes
    conn.commit()
    # close connection
    conn.close()
    # Clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    adress.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

#create table
#create textboxes

f_name = Entry(root,width=30)
f_name.grid(column=1, row=0, padx=20)
l_name = Entry(root,width=30)
l_name.grid(column=1, row=1, padx=20)
adress = Entry(root,width=30)
adress.grid(column=1, row=2, padx=20)
city = Entry(root,width=30)
city.grid(column=1, row=3, padx=20)
state = Entry(root,width=30)
state.grid(column=1, row=4, padx=20)
zipcode = Entry(root,width=30)
zipcode.grid(column=1, row=5, padx=20)

#Create text box labels
f_name_label =Label(root,text="First Name")
f_name_label.grid(row=0, column=0)
l_name_label =Label(root,text="Last Name")
l_name_label.grid(row=1, column=0)
adress_label =Label(root,text="Adress")
adress_label.grid(row=2, column=0)
city_label =Label(root,text="City")
city_label.grid(row=3, column=0)
state_label =Label(root,text="State")
state_label.grid(row=4, column=0)
zipcode_label =Label(root,text="Zipcode")
zipcode_label.grid(row=5, column=0)
#Create Submit Button
submit_btn = Button(root,text="Add record to database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

def query():
    # create our database or connect to one
    conn = sqlite3.connect('address_book.db')
    # create a cursor
    c = conn.cursor()
    #Query the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    #print(records)
    #loop through reseults
    print_records=''
    for record in records:
        print_records += str(record[0]) + " "+ str(record[1]) + "\n" + " " + str(record[2])

    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)

    # to update changes to databases
    # commit changes
    conn.commit()
    # close connection
    conn.close()
#Create query button
query_btn = Button(root, text="Show records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

root.mainloop()