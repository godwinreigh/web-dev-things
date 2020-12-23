from tkinter import *
import sqlite3

root = Tk()
root.geometry("50x50")
root.title("Database App")
second = Toplevel()
#Create a button that creates table
def table():
    global entry
    conn = sqlite3.connect(entry.get()+".db")
    # create a cursor
    c = conn.cursor()
    # create table
    c.execute("""CREATE TABLE addresses (
            first_name text,
            last_name text,
            address text,
            city text,
            state text,
            zipcode integer
            )""")

    # to update changes to databases
    # commit changes
    conn.commit()
    # close connection
    conn.close()
    entry.delete(0, END)

    next()
btn= Button(root,text="Create A table", command=table)
entry = Entry(root, text="Name of the database")
btn.grid(row=0, column=0)
entry.grid(row=1, column=0)

def query():
    global second
    global entry
    # create our database or connect to one
    conn = sqlite3.connect(entry.get()+".db")
    # create a cursor
    c = conn.cursor()
    # Query the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    # print(records)
    # loop through reseults
    print_records = ''
    for record in records:
        print_records += str(record[6]) + "\t" + str(record[0]) + " " + str(record[1]) + " " + "\n"

    query_label = Label(second, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)

    # to update changes to databases
    # commit changes
    conn.commit()
    # close connection
    conn.close()


# create a function to delete a record
def delete():
    global second
    global entry
    # create our database or connect to one
    conn = sqlite3.connect(entry.get()+".db")
    # create a cursor
    c = conn.cursor()
    # delete a record
    c.execute("DELETE from addresses WHERE oid=" + delete_box.get())
    conn.commit()
    # close connection
    conn.close()
    delete_box.delete(0, END)


# Create edit function to update a record
def update():
    global second
    global entry
    conn = sqlite3.connect(entry.get()+".db")
    # create a cursor
    c = conn.cursor()
    record_id = delete_box.get()

    c.execute("""UPDATE addresses SET
    first_name= :first,
    last_name= :last,
    address= :address,
    city = :city,
    state = :state,
    zipcode = :zipcode

    WHERE oid = :oid""",
    {
     'first': f_name_editor.get(),
     'last': l_name_editor.get(),
     'address': address_editor.get(),
     'city': city_editor.get(),
     'state': state_editor.get(),
     'zipcode': zipcode_editor.get(),
     'oid': record_id
    })
    conn.commit()
    # close connection
    conn.close()
    # clear the text boxes
    editor.destroy()


def edit():
    global second
    global entry
    global editor
    editor = Tk()
    editor.title("Update a record")
    editor.geometry("400x400")
    # create our database or connect to one
    conn = sqlite3.connect(entry.get()+".db")
    # create a cursor
    c = conn.cursor()
    record_id = delete_box.get()
    # Query the database
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()
    # Create global variables for text box names
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(column=1, row=0, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(column=1, row=1, padx=20)
    address_editor = Entry(editor, width=30)
    address_editor.grid(column=1, row=2, padx=20)
    city_editor = Entry(editor, width=30)
    city_editor.grid(column=1, row=3, padx=20)
    state_editor = Entry(editor, width=30)
    state_editor.grid(column=1, row=4, padx=20)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(column=1, row=5, padx=20)

    # Create text box labels
    f_name_label_editor = Label(editor, text="First Name")
    f_name_label_editor.grid(row=0, column=0, pady=(10, 0))
    l_name_label_editor = Label(editor, text="Last Name")
    l_name_label_editor.grid(row=1, column=0)
    address_label_editor = Label(editor, text="Adress")
    address_label_editor.grid(row=2, column=0)
    city_label_editor = Label(editor, text="City")
    city_label_editor.grid(row=3, column=0)
    state_label_editor = Label(editor, text="State")
    state_label_editor.grid(row=4, column=0)
    zipcode_label_editor = Label(editor, text="Zipcode")
    zipcode_label_editor.grid(row=5, column=0)
    # Create save button to save edited record
    save_btn = Button(editor, text="Save Records", command=update)
    save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=141)

    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])


def submit():
    # create our database or connect to one
    conn = sqlite3.connect(entry.get()+".db")
    # create a cursor
    c = conn.cursor()
    # databases
    # create table
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

def next():
    global f_name
    global l_name
    global adress
    global city
    global state
    global zipcode
    global submit_btn
    global delete_btn
    global delete_box_label
    global delete_box
    # create table
    # create textboxes

    f_name = Entry(second, width=30)
    f_name.grid(column=1, row=0, padx=20, pady=(10, 0))
    l_name = Entry(second, width=30)
    l_name.grid(column=1, row=1, padx=20)
    adress = Entry(second, width=30)
    adress.grid(column=1, row=2, padx=20)
    city = Entry(second, width=30)
    city.grid(column=1, row=3, padx=20)
    state = Entry(second, width=30)
    state.grid(column=1, row=4, padx=20)
    zipcode = Entry(second, width=30)
    zipcode.grid(column=1, row=5, padx=20)

    # Create text box labels
    f_name_label = Label(second, text="First Name")
    f_name_label.grid(row=0, column=0, pady=(10, 0))
    l_name_label = Label(second, text="Last Name")
    l_name_label.grid(row=1, column=0)
    adress_label = Label(second, text="Adress")
    adress_label.grid(row=2, column=0)
    city_label = Label(second, text="City")
    city_label.grid(row=3, column=0)
    state_label = Label(second, text="State")
    state_label.grid(row=4, column=0)
    zipcode_label = Label(second, text="Zipcode")
    zipcode_label.grid(row=5, column=0)
    # Create Submit Button
    submit_btn = Button(second, text="Add record to database", command=submit)
    submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    # Create query button
    query_btn = Button(second, text="Show records", command=query)
    query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

    # create delete button
    delete_btn = Button(second, text="Delete record", command=delete)
    delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=136)
    # delete label
    delete_box = Entry(second, width=30)
    delete_box.grid(row=9, column=1)
    delete_box_label = Label(second, text="Select ID")
    delete_box_label.grid(row=9, column=0)

    # Create update button
    update_btn = Button(second, text="Edit records", command=edit)
    update_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=141)


root.mainloop()