BITS_TO_MEGABYTE = 125 ** 2
BITS_TO_GIGABYTE = 125 ** 3


def draw(ax, canvas, times, download_data, upload_data):
    label_download_speed_string = "Download Speed "
    label_upload_speed_string = "Upload Speed "
    label_speed_string = "Speed "

    if max(download_data) > BITS_TO_GIGABYTE or max(upload_data) > BITS_TO_GIGABYTE:
        label_download_speed_string += "(Gbps)"
        label_upload_speed_string += "(Gbps)"
        label_speed_string += "(Gbps)"
        download_data = list(map(lambda x: x / BITS_TO_GIGABYTE, download_data))
        upload_data = list(map(lambda x: x / BITS_TO_GIGABYTE, upload_data))
    elif max(download_data) > BITS_TO_MEGABYTE or max(upload_data) > BITS_TO_MEGABYTE:
        label_download_speed_string += "(Mbps)"
        label_upload_speed_string += "(Mbps)"
        label_speed_string += "(Mbps)"
        download_data = list(map(lambda x: x / BITS_TO_MEGABYTE, download_data))
        upload_data = list(map(lambda x: x / BITS_TO_MEGABYTE, upload_data))
    else:
        label_download_speed_string += "(Kbps)"
        label_upload_speed_string += "(Kbps)"
        label_speed_string += "(Kbps)"

    ax.clear()
    ax.plot(times, download_data, label=label_download_speed_string, color='blue')
    ax.plot(times, upload_data, label=label_upload_speed_string, color='red')
    ax.set_xlabel("Time (seconds)")
    ax.set_ylabel(label_speed_string)

    num_points = len(times)  # Current number of points
    print(f"num_points: {num_points}")
    x_ticks = list(range(0, num_points, 5))  # Tick positions match indexes
    x_labels = x_ticks[::-1]  # Countdown from 60

    print(f"x_ticks: {x_ticks}")
    print(f"x_labels: {x_labels}")
    ax.set_xticks(x_ticks)  # Set tick positions
    ax.set_xticklabels(x_labels)  # Set countdown labels

    ax.set_title("Real-Time Bandwidth Usage")
    ax.legend()
    ax.grid(True)

    canvas.draw()
