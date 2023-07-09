import tkinter as tk
from tkinter import messagebox, font

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task_number):
        try:
            self.tasks.pop(task_number - 1)
        except IndexError:
            messagebox.showerror("Error", "Invalid task number. Please try again.")

    def view_tasks(self):
        return '\n'.join(f"{i+1}. {task}" for i, task in enumerate(self.tasks))

def main():
    to_do_list = ToDoList()

    root = tk.Tk()
    root.title("To-Do List")

    custom_font = font.Font(size=12)

    root.configure(bg='lightgray')
    tasks_text = tk.StringVar()

    def add_task():
        task = task_entry.get()
        if task:
            to_do_list.add_task(task)
            tasks_text.set(to_do_list.view_tasks())
            task_entry.delete(0, tk.END)

    def delete_task():
        task_number = task_number_entry.get()
        if task_number:
            to_do_list.delete_task(int(task_number))
            tasks_text.set(to_do_list.view_tasks())
            task_number_entry.delete(0, tk.END)

    task_label = tk.Label(root, text="Enter a task:", font=custom_font, bg='lightgray', fg='black')
    task_label.pack(padx=10, pady=10)

    task_entry = tk.Entry(root, font=custom_font)
    task_entry.pack(padx=10, pady=10)

    add_task_button = tk.Button(root, text="Add Task", command=add_task, font=custom_font, bg='darkgray', fg='white')
    add_task_button.pack(padx=10, pady=10)

    task_number_label = tk.Label(root, text="Enter the task number to delete:", font=custom_font, bg='lightgray', fg='black')
    task_number_label.pack(padx=10, pady=10)

    task_number_entry = tk.Entry(root, font=custom_font)
    task_number_entry.pack(padx=10, pady=10)

    delete_task_button = tk.Button(root, text="Delete Task", command=delete_task, font=custom_font, bg='darkgray', fg='white')
    delete_task_button.pack(padx=10, pady=10)

    tasks_label = tk.Label(root, textvariable=tasks_text, font=custom_font, bg='lightgray', fg='black')
    tasks_label.pack(padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
