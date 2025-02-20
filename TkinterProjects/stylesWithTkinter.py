import tkinter as tk
from tkinter import ttk


root = tk.Tk()
style = ttk.Style(root)

style.configure("CustomEntryStyle.TEntry", padding=20)

name = ttk.Label(root, text="Hello world!!!")
entry = ttk.Entry(root, width=15)
entry["style"] = "CustomEntryStyle.TEntry"
name.pack()
entry.pack()

print(style.layout("TLabel"))

print(style.element_options("Label.border"))
print(style.element_options("Label.padding"))
print(style.element_options("Label.label"))

print(style.lookup("TLabel", "font"))
print(style.lookup("TLabel", "foreground"))
print(style.lookup("TLabel", "compound"))



root.mainloop()
