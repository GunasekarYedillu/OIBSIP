import tkinter as tk
from tkinter import messagebox
import string
import random

def generate_password(min_length, numbers=True, special_characters=True):
    s1 = string.ascii_letters
    s2 = string.digits
    s3 = string.punctuation

    characters = s1
    if numbers:
        characters += s2
    if special_characters:
        characters += s3

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in s2:
            has_number = True
        elif new_char in s3:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd

def generate_and_display_password():
    try:
        min_length = int(length_entry.get())
        has_number = number_var.get()
        has_special = special_var.get()
        
        if min_length <= 0:
            raise ValueError("Length must be greater than 0.")
        
        pwd = generate_password(min_length, has_number, has_special)
        result_label.config(text=f"Your password is: {pwd}")
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

# Create the main window
root = tk.Tk()
root.title("GUNAS Password Generator")
root.geometry("400x300")
root.configure(bg="lightblue")

# Create a frame to center the contents
frame = tk.Frame(root, bg="lightblue")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Title label with bold font
title_label = tk.Label(frame, text="GUNAS Password Generator", font=("Helvetica", 16, "bold"), bg="lightblue")
title_label.pack(pady=10)

# Input for password length with bold font
length_label = tk.Label(frame, text="Enter Password Length:", bg="lightblue", font=("Helvetica", 12, "bold"))
length_label.pack(pady=5)
length_entry = tk.Entry(frame, font=("Helvetica", 12, "bold"))
length_entry.pack(pady=5)

# Checkbox for including numbers with bold font
number_var = tk.BooleanVar(value=True)  # Default to True
number_checkbox = tk.Checkbutton(frame, text="Include Numbers", variable=number_var, bg="lightblue", font=("Helvetica", 12, "bold"))
number_checkbox.pack(pady=5)

# Checkbox for including special characters with bold font
special_var = tk.BooleanVar(value=True)  # Default to True
special_checkbox = tk.Checkbutton(frame, text="Include Special Characters", variable=special_var, bg="lightblue", font=("Helvetica", 12, "bold"))
special_checkbox.pack(pady=5)

# Button to generate password with bold font
generate_button = tk.Button(frame, text="Generate Password", command=generate_and_display_password, bg="lightgreen", font=("Helvetica", 12, "bold"))
generate_button.pack(pady=10)

# Label to display the generated password with bold font
result_label = tk.Label(frame, text="", bg="lightblue", font=("Helvetica", 12, "bold"))
result_label.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()
