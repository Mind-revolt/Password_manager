from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import string
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
chars = string.ascii_letters
chars.strip()

special_chars = string.punctuation
special_chars.strip()
all_chars = []
for digit in digits:
    all_chars.append(digit)
for char in chars:
    all_chars.append(char)
for item in special_chars:
    all_chars.append(item)

# an alternative way to convert a list, int or a tuple to a string
# join function. <separator>.join(datatype) separator - can be any character
# mylist = ['John', 'Paul', 'Makabi']
# new_string = ''.join(mylist)

def password_gen():
    password = []
    for n in range(1, 12):
        n = random.choice(all_chars)
        password.append(n)
    password_str = ''
    for x in password:
        password_str += '' + x
    pyperclip.copy(password_str)
    return password_textbox.insert(0, string=password_str)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website_entry = website_textbox.get()
    email_entry = email_textbox.get()
    password_entry = password_textbox.get()
    # a nested dict to fit a json format.
    # json format enables multilevel dictionaries which can be useful for complex data usage
    new_data = {website_entry: {
                    "email": email_entry,
                    "password": password_entry,
        }
    }

    if len(website_entry) == 0 or len(email_entry) == 0 or len(password_entry) == 0:
        messagebox.showerror(title='Error', message="Entry in a textbox can't be empty")
    else:
        #     Split the data into read and write
            # read
        try:
            with open('data.json', mode='r') as data_file:
                    # to read the json file and convert it to a python dict use json.load
                    data = json.load(data_file)
                    # how to update
        except FileNotFoundError:
            # write and create a new file if it doesn't exist yet.
            with open('data.json', mode='w') as saved_file:
                json.dump(new_data, saved_file, indent=4)

        else:
            # update    - if the file can be loaded than we can update it with new data.
            # interesting enough no need for opening the file.
            data.update(new_data)

            with open('data.json', mode='w') as saved_file:
                # saving updated data
                json.dump(data, saved_file, indent=4)
        finally:
            # regardless of the state each time after clicking "add" delete the two lines (website and password).
            website_textbox.delete(0, END)
            password_textbox.delete(0, END)


            #    creating a json file and writing a nested dict in it
            # json.dump(new_data, data_file, indent=4)

# ---------------------------- SEARCH --------------------------------- #
def find_password():
    website_entry = website_textbox.get()
    email_entry = email_textbox.get()
    password_entry = password_textbox.get()
    try:
        with open('data.json') as data_file:
            data = json.load(data_file)
            if website_entry in data:
                # to get hold of data inside a nested dict use two pairs of brackets
                # it actually works and transforms the data in a dict into a string
                email = data[website_entry]['email']
                password = data[website_entry]['password']
                messagebox.askokcancel(title=f'{website_entry}',
                                                message=f"email: {email}\npassword: {password}")
            else:
                messagebox.showerror(title='Error', message="This website isn't in the password manager")
    except FileNotFoundError:
            messagebox.showerror(title='Error', message="File not found. Create it first.")
    finally:
            website_textbox.delete(0, END)

            # for key, value in data.items():
            #     if key == website_entry:
            #         messagebox.askokcancel(title='Website Found',
            #                                message=f"{str(value)}")









# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.minsize(height=400, width=400)
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)

# create canvas
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)


# Labels
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

# textboxes
website = StringVar()
website_textbox = ttk.Entry(width=41, textvariable=website)

# to bring cursor at the start to a first textbox use focus method
website_textbox.focus()
website_textbox.grid(column=1, row=1, columnspan=2)

email_textbox = Entry(width=41)
# to start with a text use insert method. index=0 means first character of the line,
# End means you can type from last character
email_textbox.insert(0, 'greenindigoman@proton.me')
email_textbox.grid(column=1, row=2, columnspan=2)

password_textbox = Entry(width=22)
password_textbox.grid(column=1, row=3)

# Buttons
gen_password_button = Button(text='Generate Password', width=15, command=password_gen)
gen_password_button.grid(column=2, row=3)
add_button = Button(text='Add', width=38, command=add)
add_button.grid(column=1, row=4, columnspan=2)
search_button = Button(text='Search', width=15, command=find_password)
search_button.grid(column=2, row=1)


window.mainloop()



