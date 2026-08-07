import tkinter as tk

class ChannelPanel(tk.Frame):
    def __init__(self, parent, dmx=None, channels=16):
        super().__init__(parent)
        self.dmx = dmx
        self.sliders = []
        self.selected_channel = 1

        for channel in range(1, channels + 1):
            frame = tk.Frame(self)
            frame.pack(fill='x')

            label = tk.Label(frame, text=f'CH {channel}')
            label.pack(side='left')

            value = tk.IntVar(value=0)
            slider = tk.Scale(
                frame,
                from_=0,
                to=255,
                orient='horizontal',
                variable=value,
                command=lambda v, ch=channel: self.change_channel(ch, v)
            )
            slider.pack(fill='x', expand=True)

            self.sliders.append((slider, value))

    def change_channel(self, channel, value):
        self.selected_channel = channel
        if self.dmx:
            self.dmx.set_channel(channel, int(float(value)))

    def set_selected(self, channel):
        if 1 <= channel <= len(self.sliders):
            self.selected_channel = channel
