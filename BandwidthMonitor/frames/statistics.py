import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from frames.database import get_last_minutes_data

from frames.animation import draw
from frames.style_constants import *


class Statistics(ttk.Frame):
    def __init__(self, master, show_live_updates):
        super().__init__(master)

        self["style"] = "Background.TFrame"

        statistics_frame = ttk.Frame(self, style="Monitor.TFrame")
        statistics_frame.grid(row=0, column=0, columnspan=2, pady=(10, 0), sticky="NSEW")

        live_updates_button = ttk.Button(statistics_frame,
                                         text="Live Updates",
                                         command=show_live_updates,
                                         style="MonitorButton.TButton",
                                         cursor="hand2")
        live_updates_button.grid(row=0, column=0, sticky="W", padx=10, pady=10)

        self.statistics_option = tk.StringVar(self)
        self.menu_options = ("Last 5 minutes", "Last 1 hour", "Last 12 hours", "Last 24 hours")
        option_menu = ttk.OptionMenu(self, self.statistics_option, self.menu_options[0], *self.menu_options,
                                     command=self.options_changed, style="MonitorButton.TButton")
        option_menu.grid(row=0, column=1, sticky="E", padx=10, pady=10)


        # Plot initialization
        self.fig, self.ax = plt.subplots(figsize=(6, 4))
        self.fig.patch.set_facecolor(COLOUR_PRIMARY)
        self.canvas = FigureCanvasTkAgg(self.fig, master=statistics_frame)
        self.canvas.get_tk_widget().grid(row=1, column=0, columnspan=2, pady=10, padx=10)

        self.animate_statistics(5)

    def options_changed(self, *args):
        print(self.statistics_option.get())
        if self.statistics_option.get() == "Last 5 minutes":
            self.animate_statistics(5)
        elif self.statistics_option.get() == "Last 1 hour":
            self.animate_statistics(60)
        elif self.statistics_option.get() == "Last 12 hours":
            self.animate_statistics(60 * 12)
        elif self.statistics_option.get() == "Last 24 hours":
            self.animate_statistics(60 * 24)

    def animate_statistics(self, last_n_minutes):
        net_data = get_last_minutes_data(last_n_minutes)
        print(f"Net data: {net_data}")
        past_times = list(range(len(net_data)))
        past_download_data = list(map(lambda item: item[1], net_data))
        past_upload_data = list(map(lambda item: item[2], net_data))

        self.ax.clear()
        self.ax.set_title("Statistics", color=COLOUR_LIGHT_TEXT)
        draw(
            self.ax,
            self.canvas,
            past_times,
            past_download_data,
            past_upload_data)
