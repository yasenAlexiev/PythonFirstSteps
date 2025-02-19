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


def animate_live_graph(plot_properties):
    while True:
        print("animate_live_graph")
        sleep(1)
        _, ax, canvas = plot_properties
        ax.clear()
        ax.plot(times, download_data, label="Download Speed (Mbps)", color='blue')
        ax.plot(times, upload_data, label="Upload Speed (Mbps)", color='red')

        ax.set_xlabel("Time (seconds)")
        ax.set_ylabel("Speed (Mbps)")

        ax.set_title("Real-Time Bandwidth Usage")
        ax.legend()
        ax.grid(True)
        canvas.draw()


def on_select(plot_properties, plot_type):
    _, ax, canvas = plot_properties
    print(plot_type)
    if plot_type == "Life Plot":
        animate_live_graph()
    elif plot_type == "Statistic from last 24 hour":
        animate_statistics(ax, canvas)


def create_buttons(root, plot_properties):
    _, ax, canvas = plot_properties
    animate_live_graph(plot_properties)

    # Create buttons to swap between the plots
    button_sine = tk.Button(root, text="Life Plot", command=lambda: on_select(plot_properties, "Life Plot"))
    button_sine.pack(side=tk.LEFT, padx=10)

    button_cosine = tk.Button(root, text="Statistic from last 24 hour",
                              command=lambda: on_select(plot_properties, "Statistic from last 24 hour"))
    button_cosine.pack(side=tk.LEFT, padx=10)
