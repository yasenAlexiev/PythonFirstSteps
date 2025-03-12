import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from collections import deque
import psutil
from datetime import datetime

from frames.database import get_last_minutes_data, DATE_FORMAT, commit_data, read_data
from frames.animation import draw

from frames.style_constants import *

# Number of data points to show on the graph
MAX_POINTS = 60
BITS_TO_KILOBYTE = 125
BITS_TO_MEGABYTE = 125 ** 2


class LiveUpdate(ttk.Frame):
    def __init__(self, master, show_statistics):
        super().__init__(master)

        self["style"] = "Background.TFrame"
        self["borderwidth"] = 5
        self["relief"] = "ridge"
        self.current_net_info = psutil.net_io_counters()
        self.times = deque(range(0, MAX_POINTS), maxlen=MAX_POINTS)
        self.upload_data = deque([0] * MAX_POINTS, maxlen=MAX_POINTS)
        self.download_data = deque([0] * MAX_POINTS, maxlen=MAX_POINTS)
        self.sum_for_hour_download = 0
        self.sum_for_hour_upload = 0
        self.current_step = 0

        statistics_button = ttk.Button(self,
                                       text="Statistics",
                                       command=show_statistics,
                                       style="MonitorButton.TButton",
                                       cursor="hand2")
        statistics_button.grid(row=0, column=1, sticky="E", padx=10, pady=10)

        # Plot initialization
        self.fig, self.ax = plt.subplots(figsize=(6, 4))
        self.fig.patch.set_facecolor(COLOUR_PRIMARY)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().grid(row=1, column=0, columnspan=2, pady=10, padx=10)

        self.update_live_data()

    def update_live_data(self):
        past_net_info = self.current_net_info
        self.current_net_info = psutil.net_io_counters()

        upload_bytes_per_second = self.current_net_info.bytes_sent - past_net_info.bytes_sent
        download_bytes_per_second = self.current_net_info.bytes_recv - past_net_info.bytes_recv

        self.upload_data.append(upload_bytes_per_second / BITS_TO_KILOBYTE)
        self.download_data.append(download_bytes_per_second / BITS_TO_KILOBYTE)

        self.ax.clear()
        self.ax.set_title("Real-Time Bandwidth Usage", color=COLOUR_LIGHT_TEXT)
        draw(
            self.ax,
            self.canvas,
            self.times,
            self.download_data,
            self.upload_data)

        if self.current_step % MAX_POINTS == 0:
            self.sum_for_hour_download += sum(self.download_data)
            self.sum_for_hour_upload += sum(self.upload_data)
            self.log_information()
            self.sum_for_hour_download = 0
            self.sum_for_hour_upload = 0

        self.current_step += 1
        self.after(1000, self.update_live_data)

    def log_information(self):
        date = datetime.now().strftime(DATE_FORMAT)
        commit_data(date, self.sum_for_hour_download, self.sum_for_hour_upload)
