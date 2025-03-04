import tkinter as tk
import tkinter.ttk as ttk

class Statistics(tk.Frame):
    def __init__(self, master, show_live_updates):
        super().__init__(master)

        live_updates_button = ttk.Button(self,
                                       text="Live Updates",
                                       command=show_live_updates,
                                       cursor="hand2")
        live_updates_button.grid(row=0, column=1, sticky="E", padx=10, pady=10)

        live_updates_frame = ttk.Frame(self, height="100")
        live_updates_frame.grid(row=1, column=0, columnspan=2, pady=(10, 0), sticky="NSEW")
