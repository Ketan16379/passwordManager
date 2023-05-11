from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_user_input.insert(0, password)
    pyperclip.copy(password)

    # password = "".join(password_list)
    # password_entry.insert(0, password)
    # pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    new_data = {
        website_user_input.get(): {
            "email": email_username_user_input.get(),
            "password": password_user_input.get(),
        }}

    if len(website_user_input.get()) == 0 or len(email_username_user_input.get()) == 0 or len(
            password_user_input.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please fill all the required fields.")
    else:
        # is_ok = messagebox.askokcancel(title="website", message=f"This are the details entered: \nEmail: {email_username_user_input.get()}\n Password:{password_user_input.get()} \n"
        #                                                         f"Is it ok to save?")
        # if is_ok:
        #     with open("data.txt", "a") as data:
        #         data.write(f"{website_user_input.get()} | {email_username_user_input.get()} | {password_user_input.get()}")
        #         data.write("\n")
        #
        #         website_user_input.delete(0, END)
        #         email_username_user_input.delete(0, END)
        #         password_user_input.delete(0, END)

        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        finally:
            website_user_input.delete(0, END)
            password_user_input.delete(0, END)
#-----------------------------SEARCH------------------------------------#

def search():

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Alert", message="No Data Found")

    else:
        for web_name in data:
            if (website_user_input.get() == web_name):
                email = data[web_name]["email"]
                password = data[web_name]["password"]
                messagebox.showinfo(title=f"f{web_name}", message=f"Email: {email}\nPassword: {password}")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.minsize(width=100, height=100)
window.title("Passward Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

website_lable = Label(text="Website: ")
website_lable.grid(row=1, column=0)

website_user_input = Entry(width=30)
website_user_input.focus()
website_user_input.get()
website_user_input.grid(row=1, column=1, columnspan=1)

email_username = Label(text="Email/Username:")
email_username.grid(row=2, column=0)

email_username_user_input = Entry(width=36)
email_username_user_input.get()
email_username_user_input.insert(0, "ketanmeshram184@gmail.com")
email_username_user_input.grid(row=2, column=1, columnspan=2)

password = Label(text="Password: ")
password.grid(row=3, column=0)

password_user_input = Entry(width=21)
password_user_input.get()
password_user_input.grid(row=3, column=1, columnspan=2)

generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(row=3, column=2)

search_button = Button(text="Search", width=13, command=search)
search_button.grid(row=1, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()
