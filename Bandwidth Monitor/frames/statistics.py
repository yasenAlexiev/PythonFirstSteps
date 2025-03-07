import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from frames.database import get_last_minutes_data

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

        # Plot initialization
        self.fig, self.ax = plt.subplots(figsize=(6, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().grid(row=1, column=0, columnspan=2, pady=10, padx=10)

        # Toolbar (Optional, remove if not needed)
        toolbar = NavigationToolbar2Tk(self.canvas, self, pack_toolbar=False)
        toolbar.grid(row=2, column=0, columnspan=2)

        self.animate_statistics()


    def animate_statistics(self):
        net_data = get_last_minutes_data(5)

        print(f"net_data: {net_data}")

        past_times = list(range(len(net_data)))
        past_download_data = list(map(lambda item: item[1], net_data))
        past_upload_data = list(map(lambda item: item[2], net_data))

        self.ax.clear()
        self.ax.plot(past_times, past_download_data, label="Download Speed (Mbps)", color='blue')
        self.ax.plot(past_times, past_upload_data, label="Upload Speed (Mbps)", color='red')

        self.canvas.draw()