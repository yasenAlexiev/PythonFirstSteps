import tkinter as tk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from live_calculations import *


def create_window():
    root = tk.Tk()
    root.title("Bandwidth Monitor")
    return root


def create_multiplot_figure(root):
    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, root)
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    return fig, ax, canvas


def animate_statistics(ax, canvas):
    net_data = get_last_minutes_data(5)

    past_times = list(range(len(net_data)))
    past_download_data = list(map(lambda item: item[1], net_data))
    past_upload_data = list(map(lambda item: item[2], net_data))

    ax.clear()
    ax.plot(past_times, past_download_data, label="Download Speed (Mbps)", color='blue')
    ax.plot(past_times, past_upload_data, label="Upload Speed (Mbps)", color='red')

    canvas.draw()


