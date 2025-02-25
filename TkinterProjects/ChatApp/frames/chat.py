import tkinter as tk
from tkinter import ttk
import requests
from frames.message_window import MessageWindow

messages = [{"message": "Hello, world!", "date": 15498487}]
message_labels = []


class Chat(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.messages_window = MessageWindow(self)
        self.messages_window.grid(row=0, column=0, sticky="NSEW", padx=5)

        input_frame = ttk.Frame(self, padding=10)
        input_frame.grid(row=1, column=0, sticky="EW")

        message_fetch = ttk.Button(
            input_frame,
            text="Fetch",
            command=self.get_messages
        )
        message_fetch.pack()
        self.messages_window.update_message_widgets(message_labels, messages)

    def get_messages(self):
        global messages
        messages = requests.get("http://167.99.63.70/messages").json()
        self.messages_window.update_message_widgets(message_labels, messages)
