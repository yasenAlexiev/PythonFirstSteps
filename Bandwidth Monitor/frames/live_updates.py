import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from collections import deque
from time import sleep
import time
import psutil

# Number of data points to show on the graph
MAX_POINTS = 60
SECONDS_ON_GRAPH = 60
BITS_TO_MEGABIT = 125 ** 2


class LiveUpdate(tk.Frame):
    def __init__(self, master, show_statistics):
        super().__init__(master)

        # Initialize data storage (FIFO queue for smooth scrolling effect)
        self.times = deque(maxlen=MAX_POINTS)
        self.upload_data = deque(maxlen=MAX_POINTS)
        self.download_data = deque(maxlen=MAX_POINTS)
        self.sum_for_hour_download = 0
        self.sum_for_hour_upload = 0

        statistics_button = ttk.Button(self,
                                     text="Statistics",
                                     command=show_statistics,
                                     cursor="hand2")
        statistics_button.grid(row=0, column=1, sticky="E", padx=10, pady=10)


        self.update_live_data()

    def draw(self):
        # Data for plotting
        live_updates_frame = tk.Frame()

        fig = plt.figure(figsize=(8, 8))

        fig.add_subplot(111).plot(self.times, self.upload_data)

        canvas = FigureCanvasTkAgg(fig, live_updates_frame)
        toolbar = NavigationToolbar2Tk(canvas, live_updates_frame)
        toolbar.update()
        canvas._tkcanva.grid(row=1,column=0, sticky="NSEW")

        live_updates_frame.grid(row=1, column=0, sticky="NSEW")

    def update_live_data(self):
        net_info_1 = psutil.net_io_counters()
        sleep(SECONDS_ON_GRAPH / MAX_POINTS)
        net_info_2 = psutil.net_io_counters()

        upload_bytes_1 = net_info_1.bytes_sent
        upload_bytes_2 = net_info_2.bytes_sent
        download_bytes_1 = net_info_1.bytes_recv
        download_bytes_2 = net_info_2.bytes_recv

        upload_bytes_per_second = upload_bytes_2 - upload_bytes_1
        download_bytes_per_second = download_bytes_2 - download_bytes_1

        self.times.append(int(time.time() % 60))
        self.upload_data.append(upload_bytes_per_second / BITS_TO_MEGABIT)
        self.download_data.append(download_bytes_per_second / BITS_TO_MEGABIT)

        self.draw()

        if int(time.time()) % MAX_POINTS == 0:
            self.sum_for_hour_download += sum(self.download_data)
            self.sum_for_hour_upload += sum(self.upload_data)

        if int(time.time()) % MAX_POINTS == 0:
            #log_information()
            self.sum_for_hour_download = 0
            self.sum_for_hour_upload = 0

        self._live_updates_job = self.after(1000, self.update_live_data)

