import random
import string
import tkinter as tk
from tkinter import Label, Entry, Button

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def generate_and_display_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        result_label.config(text="Please enter a valid number.")
        return

    password = generate_password(length)
    result_label.config(text="Generated Password: " + password)

# Create the main Tkinter window
root = tk.Tk()
root.title("Password Generator")

# Create and place widgets in the window
length_label = Label(root, text="Enter password length:")
length_label.pack(pady=10)

length_entry = Entry(root)
length_entry.pack(pady=10)

generate_button = Button(root, text="Generate Password", command=generate_and_display_password)
generate_button.pack(pady=20)

result_label = Label(root, text="")
result_label.pack()

# Run the Tkinter event loop
root.mainloop()
