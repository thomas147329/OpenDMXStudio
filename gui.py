import tkinter as tk


class OpenDMXStudioGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("OpenDMX Studio")
        self.root.geometry("1000x600")

        self.master = tk.Scale(
            root,
            from_=255,
            to=0,
            label="Master",
            orient="vertical"
        )
        self.master.pack(side="left", padx=20)

        self.status = tk.Label(root, text="DMX Offline")
        self.status.pack(side="bottom")

        self.channels = []
        for i in range(16):
            slider = tk.Scale(
                root,
                from_=255,
                to=0,
                label=f"CH {i+1}",
                orient="vertical"
            )
            slider.pack(side="left")
            self.channels.append(slider)
