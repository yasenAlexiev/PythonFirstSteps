import tkinter as tk
from tkinter import ttk

class Settings(tk.Frame):
    def __init__(self, parent, controller, show_timer):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        settings_container = ttk.Frame(self, padding="30 15 30 15")


        settings_container.grid(row=0, column=0, padx=10, pady=10, sticky="EW")
        settings_container.columnconfigure(0, weight=1)
        settings_container.rowconfigure(1, weight=1)

        # pomodoro label ================================================
        pomodoro_label = ttk.Label(settings_container, text="Pomodoro")
        pomodoro_label.grid(row=0, column=0, sticky="W")

        pomodoro_input = tk.Spinbox(
            settings_container,
            from_=0,
            to=120,
            increment=1,
            justify="center",
            textvariable=controller.pomodoro,
            width=10)
        pomodoro_input.grid(row=0, column=1, sticky="EW")
        pomodoro_input.focus()

        # long break label ================================================
        long_break_label = ttk.Label(settings_container, text="Long break")
        long_break_label.grid(row=1, column=0, sticky="W")

        long_break_input = tk.Spinbox(
            settings_container,
            from_=0,
            to=60,
            increment=1,
            justify="center",
            textvariable=controller.long_break,
            width=10)
        long_break_input.grid(row=1, column=1, sticky="EW")

        # short break label ================================================
        short_break_label = ttk.Label(settings_container, text="Short break")
        short_break_label.grid(row=2, column=0, sticky="W")

        short_break_input = tk.Spinbox(
            settings_container,
            from_=0,
            to=30,
            increment=1,
            justify="center",
            textvariable=controller.short_break,
            width=10)
        short_break_input.grid(row=2, column=1, sticky="EW")

        for child in settings_container.winfo_children():
            child.grid_configure(padx=5, pady=5)

        button_container = ttk.Frame(self)
        button_container.grid(sticky="EW", padx=10)
        button_container.columnconfigure(0, weight=1)

        timer_button = ttk.Button(button_container, command=show_timer, text="<- Back", cursor="hand2")
        timer_button.grid(row=0, column=0, sticky="EW", padx=2)