import datetime
import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk

MAX_MESSAGE_WIDTH = 800


class MessageWindow(tk.Canvas):
    def __init__(self, container, *argv, **kwargs):
        super().__init__(container, *argv, **kwargs, highlightthickness=0)

        self.message_frame = ttk.Frame(self, style="Messages.TFrame")
        self.message_frame.columnconfigure(0, weight=1)

        self.scrollable_window = self.create_window((0, 0), window=self.message_frame, anchor="nw")

        def configure_scroll_region(event):
            self.configure(scrollregion=self.bbox("all"))

        def configure_window_size(event):
            self.itemconfig(self.scrollable_window, width=self.winfo_width())

        self.bind("<Configure>", configure_window_size)
        self.message_frame.bind("<Configure>", configure_scroll_region)
        self.bind_all("<MouseWheel>", self._on_mousewheel)

        scrollbar = ttk.Scrollbar(container, orient="vertical", command=self.yview)
        scrollbar.grid(row=0, column=1, sticky="NS")

        self.configure(yscrollcommand=scrollbar.set)
        self.yview_moveto(1.0)

    def _on_mousewheel(self, event):
        self.yview_scroll(-int(event.delta/120), "units")

    def update_message_widgets(self, message_labels, messages):
        existing_labels = [
            (message["text"], time["text"]) for message, time in message_labels]

        for message in messages:
            message_time = datetime.datetime.fromtimestamp(message["date"]).strftime(
                "%d-%m-%Y %H:%M:%S"
            )

            if (message["message"], message_time) not in existing_labels:
                self._create_message_container(message["message"], message_time, message_labels)

    def _create_message_container(self, message_content, message_time, message_labels):
        container = ttk.Frame(self.message_frame, style="Messages.TFrame")
        container.columnconfigure(1, weight=1)
        container.grid(sticky="EW", padx=(10, 50), pady=10)

        def reconfigure_message_labels(event):
            for label, _ in message_labels:
                label.configure(wraplength=min(container.winfo_width() - 130, MAX_MESSAGE_WIDTH))

        container.bind("<Configure>", reconfigure_message_labels)

        self._create_message_bubble(container, message_content, message_time, message_labels)

    def _create_message_bubble(self, container, message_content, message_time, message_labels):
        avatar_image = Image.open("./assets/male_avatar.png")
        avatar_photo = ImageTk.PhotoImage(avatar_image)

        avatar_label = ttk.Label(container, image=avatar_photo, style="Avatar.TLabel")
        avatar_label.image = avatar_photo
        avatar_label.grid(row=0, column=0,
                          rowspan=2, sticky="NEW",
                          padx=(0, 10), pady=(5, 0))

        time_label = ttk.Label(
            container,
            text=message_time,
            style="Time.TLabel"
        )
        time_label.grid(row=0, column=1, sticky="NEW")
        message_label = ttk.Label(
            container,
            text=message_content,
            anchor="w",
            justify="left",
            style="Message.TLabel"
        )
        message_label.grid(row=1, column=1, sticky="NSEW")

        message_labels.append((message_label, time_label))
