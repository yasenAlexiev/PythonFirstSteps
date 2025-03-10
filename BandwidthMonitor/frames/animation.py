

def draw(ax, canvas, times, download_data, upload_data):
    ax.clear()
    ax.plot(times, download_data, label="Download Speed (Mbps)", color='blue')
    ax.plot(times, upload_data, label="Upload Speed (Mbps)", color='red')
    ax.set_xlabel("Time (seconds)")
    ax.set_ylabel("Speed (Mbps)")
    ax.set_title("Real-Time Bandwidth Usage")
    ax.legend()
    ax.grid(True)

    canvas.draw()
