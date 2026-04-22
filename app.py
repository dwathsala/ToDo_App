import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("ToDo App")
root.geometry('400x500')
root.resizable(False,False)
root.iconbitmap('check.ico')

heading = ttk.Label(root, text='All TASKS', font='arial 20 bold', foreground='darkblue')
heading.pack()

frame = ttk.Frame(root, width=400, height=50)
frame.pack(pady=2) 

task_entry = ttk.Entry(frame, font='arial 18', width=27)
task_entry.pack()

frame1 = ttk.Frame(root, width=300, height=250)
frame1.pack(pady=10)

listbox = tk.Listbox(frame1, font='arial 12', width=39, height=18)
listbox.pack()

s = ttk.Style()
s.configure('TButton', font='arial 12', foreground='red')

delete_btn = ttk.Button(root, text='Delete Task', style='TButton')
delete_btn.pack(pady=12,ipadx=10,ipady=12, side=tk.BOTTOM)

root.mainloop()