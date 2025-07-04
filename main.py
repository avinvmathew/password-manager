from tkinter import *
FONT = ("Comic Sans MS", 10)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="ew")

#Buttons
generate_pwd_button = Button(text="Generate Password")
generate_pwd_button.grid(row=3, column=2, sticky="ew")

add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")

#entry acquisition and writing to file




window.mainloop()