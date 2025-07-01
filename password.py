import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(entry_length.get())
        if length < 4:
            messagebox.showwarning("Too short", "Password length should be at least 4 characters.")
            return

        # Characters to use
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# GUI setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.config(bg="#1e1e2f")  # Dark background

# Title
tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"),
         bg="#1e1e2f", fg="white").pack(pady=10)

# Password length input
tk.Label(root, text="Enter password length:", bg="#1e1e2f", fg="white").pack()
entry_length = tk.Entry(root, width=10, justify="center", bg="#f5f6fa", fg="#2d3436")
entry_length.pack(pady=5)

# Generate button
tk.Button(root, text="Generate Password", command=generate_password,
          bg="#00b894", fg="white", activebackground="#019875").pack(pady=10)

# Password display
tk.Label(root, text="Generated Password:", bg="#1e1e2f", fg="white").pack()
entry_password = tk.Entry(root, width=35, font=("Arial", 12), justify="center",
                          bg="#f5f6fa", fg="#2d3436")
entry_password.pack(pady=5)

# Run the app
root.mainloop()
