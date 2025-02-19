from collections import deque
from datetime import datetime
from database import *
from time import sleep
import time
import psutil

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
    date = datetime.datetime.today().strftime(DATE_FORMAT)

    commit_data(date, sum_for_hour_download, sum_for_hour_upload)

    read_data()
    get_last_minutes_data(5)


def update_live_data():
    global times, upload_data, download_data, sum_for_hour_download, sum_for_hour_upload
    while True:
        print("running")
        net_info_1 = psutil.net_io_counters()
        sleep(SECONDS_ON_GRAPH / MAX_POINTS)
        net_info_2 = psutil.net_io_counters()

        upload_bytes_1 = net_info_1.bytes_sent
        upload_bytes_2 = net_info_2.bytes_sent
        download_bytes_1 = net_info_1.bytes_recv
        download_bytes_2 = net_info_2.bytes_recv

        upload_bytes_per_second = upload_bytes_2 - upload_bytes_1
        download_bytes_per_second = download_bytes_2 - download_bytes_1

        times.append(int(time.time() % 60))
        upload_data.append(upload_bytes_per_second / BITS_TO_MEGABIT)
        download_data.append(download_bytes_per_second / BITS_TO_MEGABIT)
        
        if int(time.time()) % MAX_POINTS == 0:
            sum_for_hour_download += sum(download_data)
            sum_for_hour_upload += sum(upload_data)

        if int(time.time()) % MAX_POINTS == 0:
            log_information()
            sum_for_hour_download = 0
            sum_for_hour_upload = 0
