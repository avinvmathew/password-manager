from tkinter import *
from datetime import datetime
from tkinter import messagebox
from PassGenerator import PassGen
import pyperclip

FONT = ("Comic Sans MS", 10)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_generator = PassGen()
    password_entry.delete(0,END)
    new_pwd = password_generator.generate_password()
    pyperclip.copy(new_pwd)
    password_entry.insert(index=0, string=new_pwd)

# ---------------------------- SAVE PASSWORD ------------------------------- #

#writing to file
def save_to_file():
    current_datetime = datetime.now()
    website_1 = website_entry.get()
    username_2 = username_entry.get()
    password_3 = password_entry.get()

    if len(website_1) == 0 or len(username_2) == 0 or len(password_3) == 0:
        messagebox.showinfo(title="Fields empty!", message="Please don't leave any fields empty!")
    else:
        is_user_ok = messagebox.askokcancel(title=f"{website_1}", message=f"Please confirm your entry!\nUsername/email: {username_2}\nPassword: {password_3}")
        if is_user_ok:
            with open("pwd_data.txt", "a+") as file:
                file.write(f"Website: {website_1} | Username/Email: {username_2} | Password: {password_3} => added on/at : {current_datetime}\n")
            print("Password saved!")
            website_entry.delete(0,END)
            # username_entry.delete(0,END)
            password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.option_add("*Font",FONT)
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image = logo)
canvas.grid(row=0,column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1,columnspan=2, sticky="ew")
website_entry.focus()

username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2, sticky="ew")
username_entry.insert(0,"mandalorian@gmail.com")

# password_entry = Entry(width=21, show="*")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="ew")

#Buttons
generate_pwd_button = Button(text="Generate Password", command=generate_password)
generate_pwd_button.grid(row=3, column=2, sticky="ew")

add_button = Button(text="Add", width=36, command=save_to_file)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")



window.mainloop()