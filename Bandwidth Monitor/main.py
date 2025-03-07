import tkinter as tk
from tkinter import ttk
from frames import LiveUpdate, Statistics
from frames.database import create_database

class BandwidthMonitor(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Bandwidth Monitor")
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
            frame.animate_statistics()
        frame.tkraise()


root = BandwidthMonitor()
root.mainloop()
