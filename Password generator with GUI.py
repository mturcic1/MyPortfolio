import tkinter
from tkinter import messagebox
import random
#import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', "w", 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    word_list = [random.choice(letters) for letter in range(random.randint(8, 10))]
    number_list = [random.choice(numbers) for number in range(random.randint(2, 4))]
    symbol_list = [random.choice(symbols) for symbol in range(random.randint(2, 4))]

    password_list = word_list + number_list + symbol_list
    random.shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(0, password)
    #pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def main_function():
    saved_website = entry_website.get()
    saved_email = entry_email.get()
    saved_password = entry_password.get()
    new_data = {saved_website: {"email": saved_email,
                                "password": saved_password}}
    if len(saved_website) == 0 or len(saved_password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any empty fields!")
    elif len(saved_website) > 0 and len(saved_password) > 0:
        is_ok = messagebox.askokcancel(title=saved_website, message=f"These are the details entered:\nWebsite: "
                                                                    f"{saved_website}\nEmail: {saved_email}\n"
                                                                    f"Saved password: {saved_password}\n"
                                                                    "Is it ok to save?")

        if is_ok:
            try:
                with open("Password file.json", "r") as directory:
                    data = json.load(directory)
                    data.update(new_data)
                with open("Password file.json", "w") as directory:
                    json.dump(data, directory, indent=4)

                    entry_website.delete(0, "end")
                    entry_password.delete(0, "end")
            except FileNotFoundError:
                with open("Password file.json", "w") as directory:
                    json.dump(new_data, directory, indent=4)

                    entry_website.delete(0, "end")
                    entry_password.delete(0, "end")


def function_search():
    saved_website = entry_website.get()
    try:
        with open("Password file.json") as directory:
            data = json.load(directory)
            if saved_website in data:
                email = data[saved_website]["email"]
                password = data[saved_website]["password"]
                messagebox.showinfo(title=f" {saved_website}", message=f"Email:{email}\nPassword: {password}")
            elif saved_website not in data:
                messagebox.showwarning(title=f"{saved_website}", message=f"{saved_website} is not in database!")
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No data file found.")


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
logo_image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=1, column=2)

# Labels
label_website = tkinter.Label(text="Website:")
label_website.grid(row=2, column=1)

label_email = tkinter.Label(text="Email/Username:")
label_email.grid(row=3, column=1)

label_password = tkinter.Label(text="Password:")
label_password.grid(row=4, column=1)

# Entries
entry_website = tkinter.Entry(width=16)
entry_website.focus()
entry_website.grid(row=2, column=2, columnspan=1)

entry_email = tkinter.Entry(width=35)
entry_email.insert(0, "mturcic1@gmail.com")
entry_email.grid(row=3, column=2, columnspan=2)

entry_password = tkinter.Entry(width=16)
entry_password.grid(row=4, column=2)

# Buttons
button_generate_password = tkinter.Button(text="Generate password", width=15, command=generate_password)
button_generate_password.grid(row=4, column=3)

button_add = tkinter.Button(text="Add", width=30, command=main_function)
button_add.grid(row=5, column=2, columnspan=2)

button_search = tkinter.Button(text="Search", width=15, command=function_search)
button_search.grid(row=2, column=3)

window.mainloop()