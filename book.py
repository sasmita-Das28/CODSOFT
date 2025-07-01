import tkinter as tk
from tkinter import messagebox

contacts = []

def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()

    if name and phone:
        contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        messagebox.showinfo("Success", "Contact added successfully!")
        clear_fields()
        view_contacts()
    else:
        messagebox.showwarning("Error", "Name and Phone are required!")

def view_contacts():
    listbox.delete(0, tk.END)
    for i, c in enumerate(contacts):
        listbox.insert(tk.END, f"{i+1}. {c['name']} - {c['phone']}")

def clear_fields():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

def on_select(event):
    try:
        index = listbox.curselection()[0]
        selected = contacts[index]
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_address.delete(0, tk.END)

        entry_name.insert(0, selected['name'])
        entry_phone.insert(0, selected['phone'])
        entry_email.insert(0, selected['email'])
        entry_address.insert(0, selected['address'])
    except:
        pass

def update_contact():
    try:
        index = listbox.curselection()[0]
        contacts[index] = {
            "name": entry_name.get(),
            "phone": entry_phone.get(),
            "email": entry_email.get(),
            "address": entry_address.get()
        }
        messagebox.showinfo("Updated", "Contact updated successfully!")
        view_contacts()
        clear_fields()
    except:
        messagebox.showwarning("Select Contact", "Please select a contact to update.")

def delete_contact():
    try:
        index = listbox.curselection()[0]
        contacts.pop(index)
        messagebox.showinfo("Deleted", "Contact deleted successfully!")
        view_contacts()
        clear_fields()
    except:
        messagebox.showwarning("Select Contact", "Please select a contact to delete.")

def search_contact():
    query = entry_search.get().lower()
    listbox.delete(0, tk.END)
    for i, c in enumerate(contacts):
        if query in c['name'].lower() or query in c['phone']:
            listbox.insert(tk.END, f"{i+1}. {c['name']} - {c['phone']}")

# ---------- UI SETUP ----------
root = tk.Tk()
root.title("Contact Book")
root.geometry("530x640")
root.config(bg="#0b1d3a")  # Dark blue background

title = tk.Label(root, text="📘 Contact Book", font=("Helvetica", 20, "bold"), bg="#0b1d3a", fg="#f0f0f0")
title.pack(pady=15)

frame_form = tk.Frame(root, bg="#0b1d3a")
frame_form.pack(pady=5)

label_style = {"bg": "#0b1d3a", "fg": "#d3e3fc", "font": ("Arial", 12)}
entry_style = {"width": 40, "font": ("Arial", 11), "bg": "#1e3d59", "fg": "#ffffff", "insertbackground": "white"}

tk.Label(frame_form, text="Name:", **label_style).grid(row=0, column=0, sticky="w", padx=10, pady=5)
entry_name = tk.Entry(frame_form, **entry_style)
entry_name.grid(row=0, column=1, pady=5)

tk.Label(frame_form, text="Phone:", **label_style).grid(row=1, column=0, sticky="w", padx=10, pady=5)
entry_phone = tk.Entry(frame_form, **entry_style)
entry_phone.grid(row=1, column=1, pady=5)

tk.Label(frame_form, text="Email:", **label_style).grid(row=2, column=0, sticky="w", padx=10, pady=5)
entry_email = tk.Entry(frame_form, **entry_style)
entry_email.grid(row=2, column=1, pady=5)

tk.Label(frame_form, text="Address:", **label_style).grid(row=3, column=0, sticky="w", padx=10, pady=5)
entry_address = tk.Entry(frame_form, **entry_style)
entry_address.grid(row=3, column=1, pady=5)

frame_buttons = tk.Frame(root, bg="#0b1d3a")
frame_buttons.pack(pady=15)

def make_button(text, cmd, col):
    return tk.Button(frame_buttons, text=text, width=10, bg=col, fg="white", font=("Arial", 10, "bold"), command=cmd)

make_button("Add", add_contact, "#28a745").grid(row=0, column=0, padx=5)
make_button("Update", update_contact, "#007bff").grid(row=0, column=1, padx=5)
make_button("Delete", delete_contact, "#dc3545").grid(row=0, column=2, padx=5)
make_button("Clear", clear_fields, "#6c757d").grid(row=0, column=3, padx=5)

frame_search = tk.Frame(root, bg="#0b1d3a")
frame_search.pack(pady=10)

entry_search = tk.Entry(frame_search, width=30, font=("Arial", 11), bg="#1e3d59", fg="white", insertbackground="white")
entry_search.grid(row=0, column=0, padx=5)
tk.Button(frame_search, text="Search", command=search_contact, bg="#007bff", fg="white", font=("Arial", 10, "bold")).grid(row=0, column=1, padx=5)
tk.Button(frame_search, text="Show All", command=view_contacts, bg="#17a2b8", fg="white", font=("Arial", 10, "bold")).grid(row=0, column=2)

listbox = tk.Listbox(root, width=60, height=12, font=("Courier New", 11), bd=2, relief="groove",
                     bg="#1e3d59", fg="white", selectbackground="#3399ff", highlightbackground="#0b1d3a")
listbox.pack(pady=15)
listbox.bind('<<ListboxSelect>>', on_select)

view_contacts()
root.mainloop()
