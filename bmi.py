import tkinter as tk
from tkinter import messagebox
import sqlite3

# Initialize the main window with a single background color
root = tk.Tk()
root.title("GUNA.BMI Calculator")
root.geometry("700x400")
root.configure(bg="#ADD8E6")  # Light blue background

# Define a bold font for all labels and buttons
bold_font = ("Helvetica", 10, "bold")
title_font = ("Helvetica", 20, "bold")  # Larger bold font for the title

# Title "GUNA.BMI" at the top
title_label = tk.Label(root, text="GUNA.BMI", font=title_font, fg="#00008B", bg="#ADD8E6")  # Dark blue text
title_label.pack(pady=20)

# Create a frame for the calculator with a matching background color
calculator_frame = tk.Frame(root, padx=20, pady=20, bg="#B0E0E6")  # Slightly darker blue
calculator_frame.place(relx=0.5, rely=0.5, anchor="center")

# Weight and Height input fields with bold labels
tk.Label(calculator_frame, text="Enter Weight (kilograms):", fg="black", bg="#B0E0E6", font=bold_font).pack(pady=5)
weight_entry = tk.Entry(calculator_frame, font=bold_font)
weight_entry.pack(pady=5)

tk.Label(calculator_frame, text="Enter Height (meters):", bg="#B0E0E6", font=bold_font).pack(pady=5)
height_entry = tk.Entry(calculator_frame, font=bold_font)
height_entry.pack(pady=5)

# Display BMI results with bold text
result_label = tk.Label(calculator_frame, text="", bg="#B0E0E6", font=bold_font)
result_label.pack(pady=10)

# BMI categories
def categorize_bmi(bmi):
    if bmi < 18.5:
        return "You're Underweight"
    elif 18.5 <= bmi < 24.9:
        return "You're Normal weight"
    elif 25 <= bmi < 29.9:
        return "You're Overweight"
    else:
        return "Obesity"

# BMI calculation function
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        if height <= 0 or weight <= 0:
            raise ValueError("Invalid input.")
        
        bmi = weight / (height ** 2)
        category = categorize_bmi(bmi)
        result_label.config(text=f"BMI: {bmi:.2f} ({category})")
        
        # Save BMI to database
        save_bmi_to_db(weight, height, bmi, category)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for weight and height.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Button to trigger BMI calculation with matching colors
calculate_button = tk.Button(calculator_frame, text="Calculate GUNA.BMI", command=calculate_bmi, bg="#FF7F50", fg="#FFFFFF", font=bold_font)  # Coral button
calculate_button.pack(pady=10)

# Initialize the database
def init_db():
    try:
        conn = sqlite3.connect('bmi_data.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS bmi_records 
                     (id INTEGER PRIMARY KEY, weight REAL, height REAL, bmi REAL, category TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
        conn.commit()
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"An error occurred while accessing the database: {e}")
    finally:
        conn.close()

# Save BMI data to the database
def save_bmi_to_db(weight, height, bmi, category):
    try:
        conn = sqlite3.connect('bmi_data.db')
        c = conn.cursor()
        c.execute("INSERT INTO bmi_records (weight, height, bmi, category) VALUES (?, ?, ?, ?)", (weight, height, bmi, category))
        conn.commit()
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"An error occurred while saving to the database: {e}")
    finally:
        conn.close()

# Initialize the database when the program starts
init_db()

root.mainloop()
