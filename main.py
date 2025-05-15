from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list += [choice(letters) for i in range(randint(8, 10))]
    password_list += [choice(symbols) for i in range(randint(2, 4))]
    password_list += [choice(numbers) for i in range(randint(2, 4))]

    shuffle(password_list)

    password = ''.join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():
    site_info=entry_site.get()
    name_info=entry_name.get()
    password_info=entry_password.get()

    if len(site_info)==0 or len(name_info)==0 or len(password_info)==0:
        messagebox.showinfo(title='Oops', message="Please don't leave any fields empty")
    else:
        is_ok=messagebox.askokcancel(title=site_info, message=f'Email: {name_info}\nPassword: {password_info}\nSure to save?')
        if is_ok:
            with open("data.txt", "a") as f:
                f.write(f"{site_info} | {name_info} | {password_info} \n")
                entry_site.delete(0, END)
                entry_password.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title('Password Manager')
window.config(padx=50,pady=50)

canvas=Canvas(width=200, height=200,highlightthickness=0)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.grid(column=1, row=0)

label1=Label(text="Website:")
label1.grid(column=0, row=1)
label2=Label(text="Email/Username:")
label2.grid(column=0, row=2)
label3=Label(text="Password:")
label3.grid(column=0, row=3)

entry_site = Entry(width=52)
entry_site.grid(column=1, row=1, columnspan=2)
entry_site.focus()
entry_name=Entry(width=52)
entry_name.grid(column=1, row=2, columnspan=2)
entry_name.insert(0, "your@gmail.com")
entry_password=Entry(width=33)
entry_password.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=save_info)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
