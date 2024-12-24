import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_task_list()
        task_entry.delete(0, tk.END)
        messagebox.showinfo("Success", f"Task '{task}' has been added.")
    else:
        messagebox.showwarning("Warning", "Task cannot be empty.")

def update_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        selected_task = tasks[selected_task_index[0]]
        new_task = task_entry.get()
        if new_task:
            tasks[selected_task_index[0]] = new_task
            update_task_list()
            task_entry.delete(0, tk.END)
            messagebox.showinfo("Success", f"Task '{selected_task}' updated to '{new_task}'.")
        else:
            messagebox.showwarning("Warning", "Updated task cannot be empty.")
    else:
        messagebox.showwarning("Warning", "Please select a task to update.")

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_to_delete = tasks.pop(selected_task_index[0])
        update_task_list()
        messagebox.showinfo("Success", f"Task '{task_to_delete}' has been deleted.")
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

def view_tasks():
    if tasks:
        all_tasks = "\n".join(tasks)
        messagebox.showinfo("All Tasks", f"Your tasks:\n{all_tasks}")
    else:
        messagebox.showinfo("No Tasks", "You have no tasks.")

# Initialize main window
root = tk.Tk()
root.title("Task Manager")
root.geometry("500x500")
root.configure(bg="#f0f8ff")

# Task list
tasks = []

# Styles
style = ttk.Style()
style.configure("TButton", font=("Arial", 10), padding=5)
style.configure("TLabel", font=("Arial", 12), background="#f0f8ff")
style.configure("TEntry", font=("Arial", 10))

# Widgets
header_label = ttk.Label(root, text="Task Manager", font=("Arial", 16, "bold"))
header_label.pack(pady=10)

frame = ttk.Frame(root)
frame.pack(pady=10)

task_entry = ttk.Entry(frame, width=40)
task_entry.grid(row=0, column=0, padx=5)

add_button = ttk.Button(frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=1, padx=5)

task_listbox = tk.Listbox(root, width=50, height=15, font=("Arial", 10), bg="#ffffff", fg="#000000", selectbackground="#87cefa")
task_listbox.pack(pady=10)

button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

update_button = ttk.Button(button_frame, text="Update Task", command=update_task)
update_button.grid(row=0, column=0, padx=10)

delete_button = ttk.Button(button_frame, text="Delete Task", command=delete_task)
delete_button.grid(row=0, column=1, padx=10)

view_button = ttk.Button(button_frame, text="View All Tasks", command=view_tasks)
view_button.grid(row=0, column=2, padx=10)

exit_button = ttk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=10)

# Run the main loop
root.mainloop()
