import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("ToDo App")
root.geometry('400x500')
root.resizable(False,False)
root.iconbitmap('check.ico')

task_list = []

def add_task(event):
    task = task_entry.get()
    task_entry.delete(0, tk.END)
    if task:
        with open('tasks.txt', 'a') as file:
            file.write(task + '\n')
        listbox.insert(tk.END, task)
        task_list.append(task)

    '''if task != '':
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)'''
    
def delete_task():
   # print(listbox.get(tk.ANCHOR))
    task = listbox.get(tk.ANCHOR)
    listbox.delete(tk.ANCHOR)
    task_list.remove(task)

def open_tasks():
    with open('tasks.txt', 'r') as file:
        tasks = file.readlines()

        print(tasks)

    for task in tasks:
        if task != '\n':
            listbox.insert(tk.END, task)
            task_list.append(task)

heading = ttk.Label(root, text='All TASKS', font='arial 20 bold', foreground='darkblue')
heading.pack()

frame = ttk.Frame(root, width=400, height=50)
frame.pack(pady=2) 

task_entry = ttk.Entry(frame, font='arial 16', width=29)
task_entry.pack()

task_entry.bind('<Return>', add_task)

frame1 = ttk.Frame(root, width=300, height=250)
frame1.pack(pady=10)

listbox = tk.Listbox(frame1, font='arial 12', width=39, height=18)
listbox.pack()

open_tasks()

s = ttk.Style()
s.configure('TButton', font='arial 12', foreground='red')

delete_btn = ttk.Button(root, text='Delete Task', style='TButton', command= delete_task)
delete_btn.pack(pady=12,ipadx=10,ipady=12, side=tk.BOTTOM)

root.mainloop()