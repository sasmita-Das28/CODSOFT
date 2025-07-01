import tkinter as tk
from tkinter import PhotoImage
import random
import os

# --- Theme Colors ---
main_bg = "#1a2e28"
button_color = "#2ecc71"
highlight_color = "#27ae60"
text_color = "white"
entry_bg = "#21443c"
listbox_bg = "#2f4f4f"

# --- Root Window ---
root = tk.Tk()
root.title("DIN KI PLANNING")
root.geometry("520x650")
root.resizable(False, False)
root.configure(bg=main_bg)

# --- Optional Background Image ---
if os.path.exists("background.png"):
    bg_img = PhotoImage(file="background.png")
    bg_label = tk.Label(root, image=bg_img)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# --- Task List ---
tasks = ["Reading Book", "Assignment", "Studying", "Playing", "Yoga"]

# --- Functions ---
def update_listbox():
    clear_listbox()
    for task in tasks:
        lb_tasks.insert("end", task)

def clear_listbox():
    lb_tasks.delete(0, "end")

def add_task():
    task = txt_input.get().strip()
    if task:
        tasks.append(task)
        update_listbox()
        txt_input.delete(0, "end")
        lbl_display.config(text="Task added successfully.")
    else:
        lbl_display.config(text="Please enter a task.")

def delete_task():
    try:
        selected_index = lb_tasks.curselection()[0]
        deleted_task = tasks.pop(selected_index)
        update_listbox()
        lbl_display.config(text=f"Deleted: {deleted_task}")
    except IndexError:
        lbl_display.config(text="Select a task to delete.")

def delete_all_tasks():
    tasks.clear()
    update_listbox()
    lbl_display.config(text="All tasks deleted.")

def sort_tasks():
    tasks.sort()
    update_listbox()
    lbl_display.config(text="Tasks sorted alphabetically.")

def choose_random():
    if tasks:
        task = random.choice(tasks)
        lbl_display.config(text=f"Suggested task: {task}")
    else:
        lbl_display.config(text="No tasks available.")

def number_of_tasks():
    lbl_display.config(text=f"Total tasks: {len(tasks)}")

def exit_app():
    root.destroy()

# --- Button Builder ---
def create_button(text, command):
    return tk.Button(root, text=text, command=command,
                     font=("Segoe UI", 10, "bold"), width=24,
                     bg=button_color, fg="white", bd=0,
                     activebackground=highlight_color, relief="flat",
                     cursor="hand2")

# --- Layout ---
tk.Label(root, text="TO-DO LIST", font=("Segoe UI", 22, "bold"),
         fg=button_color, bg=main_bg).pack(pady=15)

lbl_display = tk.Label(root, text="", font=("Segoe UI", 11),
                       bg=highlight_color, fg=text_color, width=40, height=2,
                       bd=1, relief="sunken")
lbl_display.pack(pady=5)

txt_input = tk.Entry(root, font=("Segoe UI", 12), width=38,
                     bg=entry_bg, fg="white", insertbackground="white", bd=0)
txt_input.pack(pady=10)

create_button("Add Task", add_task).pack(pady=4)
create_button("Delete Selected Task", delete_task).pack(pady=4)
create_button("Delete All Tasks", delete_all_tasks).pack(pady=4)
create_button("Sort Tasks", sort_tasks).pack(pady=4)
create_button("Choose Random Task", choose_random).pack(pady=4)
create_button("Number of Tasks", number_of_tasks).pack(pady=4)
create_button("Exit", exit_app).pack(pady=10)

lb_tasks = tk.Listbox(root, font=("Segoe UI", 11), width=45, height=10,
                      bg=listbox_bg, fg="white", bd=0,
                      selectbackground=button_color, selectforeground="black",
                      relief="flat")
lb_tasks.pack(pady=10)

# --- Start ---
update_listbox()
root.mainloop()
