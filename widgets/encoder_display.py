import tkinter as tk

class EncoderDisplay(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text='Encoder')
        self.channel = tk.StringVar(value='Channel: 1')
        self.value = tk.StringVar(value='Value: 0')

        tk.Label(self, textvariable=self.channel).pack()
        tk.Label(self, textvariable=self.value).pack()

    def update_channel(self, channel):
        self.channel.set(f'Channel: {channel}')

    def update_value(self, value):
        self.value.set(f'Value: {value}')
