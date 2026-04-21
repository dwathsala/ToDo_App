import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("ToDo App")
root.geometry('400x500')
root.resizable(False,False)
root.iconbitmap('check.ico')

heading = ttk.Label(root, text='All TASKS', font='arial 20 bold')
heading.pack()

frame = ttk.Frame(root, width=400, height=50)
frame.pack(pady=2) 

task_entry = ttk.Entry(frame, font='arial 18', width=28)
task_entry.pack()

root.mainloop()