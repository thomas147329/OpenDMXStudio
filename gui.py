import tkinter as tk

from widgets.channel_panel import ChannelPanel
from widgets.encoder_display import EncoderDisplay


class OpenDMXStudioGUI:
    def __init__(self, root, dmx=None):
        self.root = root
        self.dmx = dmx

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

        self.encoder_display = EncoderDisplay(root)
        self.encoder_display.pack(side="bottom")

        self.channel_panel = ChannelPanel(
            root,
            dmx=self.dmx,
            encoder_display=self.encoder_display
        )
        self.channel_panel.pack(side="left", fill="both", expand=True)

        self.status = tk.Label(root, text="DMX Offline")
        self.status.pack(side="bottom")
