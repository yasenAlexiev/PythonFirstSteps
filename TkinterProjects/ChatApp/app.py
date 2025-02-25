import tkinter as tk
from frames.chat import Chat


class Messanger(tk.Tk):
    def __init__(self, *argv, **kwargs):
        super().__init__(*argv, **kwargs)

        self.geometry("1200x500")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.chat_frame = Chat(self)

        self.chat_frame.grid(row=0, column=0, sticky="SNEW")


root = Messanger()
root.mainloop()