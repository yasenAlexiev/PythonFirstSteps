from time import sleep
import psutil
import matplotlib.pyplot as plt
from collections import deque
from datetime import datetime
from database import *
from animation import *

# bytes pretty-printing
from matplotlib import animation

# Number of data points to show on the graph
MAX_POINTS = 60
SECONDS_ON_GRAPH = 60
BITS_TO_MEGABIT = 125 ** 2

# Initialize data storage (FIFO queue for smooth scrolling effect)
times = deque(maxlen=MAX_POINTS)
upload_data = deque(maxlen=MAX_POINTS)
download_data = deque(maxlen=MAX_POINTS)
sum_for_hour_download = 0
sum_for_hour_upload = 0


def log_information():
    date = datetime.today().strftime('%Y-%m-%d-%H')

    commit_data(date, sum_for_hour_download, sum_for_hour_upload)


def start():
    def update(frame):
        global times, upload_data, download_data, sum_for_hour_download, sum_for_hour_upload
        net_info_1 = psutil.net_io_counters()
        sleep(SECONDS_ON_GRAPH / MAX_POINTS)
        net_info_2 = psutil.net_io_counters()

        upload_bytes_1 = net_info_1.bytes_sent
        upload_bytes_2 = net_info_2.bytes_sent
        download_bytes_1 = net_info_1.bytes_recv
        download_bytes_2 = net_info_2.bytes_recv

        upload_bytes_per_second = upload_bytes_2 - upload_bytes_1
        download_bytes_per_second = download_bytes_2 - download_bytes_1

        times.append(frame)
        upload_data.append(upload_bytes_per_second / BITS_TO_MEGABIT)
        download_data.append(download_bytes_per_second / BITS_TO_MEGABIT)

        animate_graph(ax, times, download_data, upload_data)

        print(f"Frame: {frame}")
        if frame % MAX_POINTS == 0:
            sum_for_hour_download += sum(download_data)
            sum_for_hour_upload += sum(upload_data)

        if frame % (MAX_POINTS * 60) == 0:
            log_information()
            sum_for_hour_download = 0
            sum_for_hour_upload = 0

    create_database()

    fig, ax = plt.subplots()
    animation_object = animation.FuncAnimation(fig, update, interval=1000)
    plt.show()


start()
