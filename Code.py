# Import tkinter library
import tkinter as tk
from tkinter import messagebox

# Function to add task
def add_task():

    # Get task from input box
    task = task_entry.get()

    # Check if input is empty
    if task == "":
        messagebox.showwarning("Warning", "Please enter a task")

    else:
        # Add task to listbox
        task_listbox.insert(tk.END, task)

        # Clear input box
        task_entry.delete(0, tk.END)


# Function to delete selected task
def delete_task():

    try:
        # Get selected task
        selected_task = task_listbox.curselection()

        # Delete selected task
        task_listbox.delete(selected_task)

    except:
        messagebox.showwarning("Warning", "Please select a task")


# Create main window
root = tk.Tk()

# Window title
root.title("To-Do List App")

# Window size
root.geometry("400x500")


# Heading label
title_label = tk.Label(root, text="To-Do List", font=("Arial", 20))
title_label.pack(pady=10)


# Input box
task_entry = tk.Entry(root, width=30, font=("Arial", 14))
task_entry.pack(pady=10)


# Add button
add_button = tk.Button(root, text="Add Task", width=15, command=add_task)
add_button.pack(pady=5)


# Delete button
delete_button = tk.Button(root, text="Delete Task", width=15, command=delete_task)
delete_button.pack(pady=5)


# Listbox to show tasks
task_listbox = tk.Listbox(root, width=35, height=15, font=("Arial", 12))
task_listbox.pack(pady=20)


# Run application
root.mainloop()