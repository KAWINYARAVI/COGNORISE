import tkinter as tk
from tkinter import messagebox

# Initialize the main application window
app = tk.Tk()
app.title("Simple Task Manager")
app.geometry("300x400")

# Function to add a task to the list
def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to remove a selected task from the list
def remove_task(event):
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")

# UI Elements

# Input field to enter tasks
task_entry = tk.Entry(app, width=25)
task_entry.pack(pady=10)

# Button to add a task to the list
add_task_button = tk.Button(app, text="Add Task", command=add_task)
add_task_button.pack(pady=5)

# Listbox to display the list of tasks
task_listbox = tk.Listbox(app, width=30, height=15)
task_listbox.pack(pady=20)

# Bind the listbox to the remove function on double-click
task_listbox.bind("<Double-1>", remove_task)

# Start the Tkinter event loop
app.mainloop()
