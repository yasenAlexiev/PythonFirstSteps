import numpy as np
import matplotlib.pyplot as plt
from frames.style_constants import *
BITS_TO_MEGABYTE = 125 ** 2
BITS_TO_GIGABYTE = 125 ** 3


def draw(axis, canvas, times, download_data, upload_data):
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

    axis.plot(times, download_data, label=label_download_speed_string, color=COLOUR_DOWNLOAD_DATA)
    axis.plot(times, upload_data, label=label_upload_speed_string, color=COLOUR_UPLOAD_DATA)

    # Set the borders to a given color...
    for ax in ['top', 'bottom', 'left', 'right']:
        #axis.spines[ax].set_linewidth(2.5)  # change width
        axis.spines[ax].set_color(COLOUR_LIGHT_TEXT)  # change color

    axis.set_xlabel("Time", color=COLOUR_LIGHT_TEXT)
    axis.set_ylabel(label_speed_string, color=COLOUR_LIGHT_TEXT)

    axis.tick_params(axis='x', colors=COLOUR_LIGHT_TEXT)
    axis.tick_params(axis='y', colors=COLOUR_LIGHT_TEXT)

    # Generate evenly spaced tick positions across the length of the data
    num_ticks = min(len(times), 10)  # Limit to a maximum of 10 ticks for readability
    tick_positions = np.linspace(0, len(times) - 1, num_ticks, dtype=int)
    tick_labels = [times[i] for i in tick_positions]  # Selecting labels at calculated positions

    axis.set_xticks(tick_positions)
    axis.set_xticklabels(tick_labels[::-1])

    axis.set_facecolor(COLOUR_PRIMARY)
    axis.patch.set_facecolor(COLOUR_PRIMARY)
    axis.legend()
    axis.grid(True)

    canvas.draw()
