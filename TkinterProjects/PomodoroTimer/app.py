import tkinter as tk
from collections import deque
from tkinter import ttk

from frames import Timer, Settings
from windows import set_dpi_awareness

set_dpi_awareness()

COLOUR_PRIMARY = "#2e3f4f"
COLOUR_SECONDARY = "#293846"
COLOUR_LIGHT_BACKGROUND = "#fff"
COLOUR_LIGHT_TEXT = "#eee"
COLOUR_DARK_TEXT = "#8095a8"


class PomodoroTimer(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("Timer.TFrame", background=COLOUR_LIGHT_BACKGROUND)
        style.configure("Background.TFrame", background=COLOUR_PRIMARY)

        style.configure("TimerText.TLabel",
                        background=COLOUR_LIGHT_BACKGROUND,
                        foreground=COLOUR_DARK_TEXT,
                        font="Courier 38")

        style.configure("LightText.TLabel",
                        background=COLOUR_PRIMARY,
                        foreground=COLOUR_LIGHT_TEXT)

        style.configure("PomodoroButton.TButton",
                        background=COLOUR_SECONDARY,
                        foreground=COLOUR_LIGHT_TEXT)
        style.map("PomodoroButton.TButton",
                  background=[("active", COLOUR_PRIMARY),
                              ("disabled", COLOUR_LIGHT_TEXT)])

        self["background"] = COLOUR_PRIMARY

        self.title("Pomodoro timer")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.pomodoro = tk.StringVar(value=25)
        self.long_break = tk.StringVar(value=15)
        self.short_break = tk.StringVar(value=5)
        self.timer_order = ["Pomodoro", "Short Break", "Pomodoro", "Short Break", "Pomodoro", "Long Break"]
        self.timer_schedule = deque(self.timer_order)

        container = ttk.Frame(self)
        container.grid()
        container.columnconfigure(0, weight=1)

        self.frames = dict()

        timer_frame = Timer(container, self, lambda: self.show_frame(Settings))
        timer_frame.grid(row=0, column=0, sticky="NSEW")
        settings_frame = Settings(container, self, lambda: self.show_frame(Timer))
        settings_frame.grid(row=0, column=0, sticky="NSEW")

        self.frames[Timer] = timer_frame
        self.frames[Settings] = settings_frame

        self.show_frame(Timer)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()


app = PomodoroTimer()
app.mainloop()
