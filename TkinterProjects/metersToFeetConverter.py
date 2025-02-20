import tkinter as tk
import tkinter as ttk
import tkinter.font as font
from windows import set_dpi_awareness

set_dpi_awareness()


class DistanceConverter(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Distance container")
        self.frames = dict()

        container = ttk.Frame(self)
        container.grid(padx=30, pady=15, sticky="EW")

        for FrameClass in (MetersToFeet, FeetToMeters):
            frame = FrameClass(container, self)
            frame.grid(row=0, column=0, sticky="NSEW")
            self.frames[FrameClass] = frame

        self.show_frame(MetersToFeet)

    def show_frame(self, container):
        frame = self.frames[container]
        self.bind("<Return>", frame.calculate)
        self.bind("<KP_Enter>", frame.calculate)
        frame.tkraise()


class MetersToFeet(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)

        self.meters_value = tk.StringVar()
        self.feet_value = tk.StringVar()

        meters_label = ttk.Label(self, text="Meters: ")
        meters_input = ttk.Entry(self, width=10, textvariable=self.meters_value, font=("Segoe UI", 15))
        feet_label = ttk.Label(self, text="Feet:")
        feet_display = ttk.Label(self, text="Feet shown here:", textvariable=self.feet_value)
        calc_button = ttk.Button(self, text="Calculate", command=self.calculate)
        switch_button = ttk.Button(self,
                                   text="Switch to Feet to meters calculation ",
                                   command=lambda: controller.show_frame(FeetToMeters))

        meters_label.grid(column=0, row=0, sticky="W")
        meters_input.grid(column=1, row=0, sticky="EW")
        meters_input.focus()

        feet_label.grid(column=0, row=1, sticky="W")
        feet_display.grid(column=1, row=1, sticky="EW")

        calc_button.grid(column=0, row=2, columnspan=2, sticky="EW")
        switch_button.grid(column=0, row=3, columnspan=2, sticky="EW")

        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)

    def calculate(self, *args):
        try:
            meters = float(self.meters_value.get())
            feet = meters * 3.28084
            self.feet_value.set(f"{feet:.3f}")
        except ValueError:
            pass


class FeetToMeters(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)

        self.feet_value = tk.StringVar()
        self.meters_value = tk.StringVar()

        feet_label = ttk.Label(self, text="Feet: ")
        feet_input = ttk.Entry(self, width=10, textvariable=self.feet_value, font=("Segoe UI", 15))
        meters_label = ttk.Label(self, text="Meters:")
        meters_display = ttk.Label(self, text="Meters shown here:", textvariable=self.meters_value)
        calc_button = ttk.Button(self, text="Calculate", command=self.calculate)
        switch_button = ttk.Button(self,
                                   text="Switch to meters to feet convertion",
                                   command=lambda: controller.show_frame(MetersToFeet))

        feet_label.grid(column=0, row=0, sticky="W")
        feet_input.grid(column=1, row=0, sticky="EW")
        feet_input.focus()

        meters_label.grid(column=0, row=1, sticky="W")
        meters_display.grid(column=1, row=1, sticky="EW")

        calc_button.grid(column=0, row=2, columnspan=2, sticky="EW")
        switch_button.grid(column=0, row=3, columnspan=2, sticky="EW")

        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)

    def calculate(self, *args):
        try:
            feet = float(self.feet_value.get())
            meters = feet / 3.28084
            self.meters_value.set(f"{meters:.3f}")
        except ValueError:
            pass


root = DistanceConverter()

font.nametofont("TkDefaultFont").configure(size=15)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.mainloop()
