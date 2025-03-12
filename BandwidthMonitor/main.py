import tkinter as tk
from tkinter import ttk
from frames import LiveUpdate, Statistics
from frames.database import create_database

from frames.style_constants import *

class BandwidthMonitor(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Bandwidth Monitor")
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("Monitor.TFrame", background=COLOUR_LIGHT_BACKGROUND)
        style.configure("Background.TFrame", background=COLOUR_PRIMARY)
        style.configure("MonitorText.TLabel",
                        background=COLOUR_LIGHT_BACKGROUND,
                        foreground=COLOUR_DARK_TEXT,
                        font="Courier 38")

        style.configure("LightText.TLabel",
                        background=COLOUR_PRIMARY,
                        foreground=COLOUR_LIGHT_TEXT)

        style.configure("MonitorButton.TButton",
                        background=COLOUR_SECONDARY,
                        foreground=COLOUR_LIGHT_TEXT)

        style.map("MonitorButton.TButton",
                  background=[("active", COLOUR_LIGHT_TEXT)],  # Keep background the same on hover
                  foreground=[("active", COLOUR_SECONDARY)])  # Keep text color the same

        self["background"] = COLOUR_PRIMARY



        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        container = ttk.Frame(self)
        container.grid()
        container.columnconfigure(0, weight=1)

        self.frames = dict()
        create_database()

        live_updates_frame = LiveUpdate(container, lambda: self.show_frame(Statistics))
        live_updates_frame.grid(row=0, column=0, sticky="NSEW")
        statistics_frame = Statistics(container, lambda: self.show_frame(LiveUpdate))
        statistics_frame.grid(row=0, column=0, sticky="NSEW")

        self.frames[LiveUpdate] = live_updates_frame
        self.frames[Statistics] = statistics_frame

        self.show_frame(LiveUpdate)

    def show_frame(self, container):
        frame = self.frames[container]
        if type(frame) is Statistics:
            frame.options_changed()
        frame.tkraise()


root = BandwidthMonitor()
root.mainloop()
