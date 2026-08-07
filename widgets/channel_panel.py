import tkinter as tk


class ChannelPanel(tk.Frame):
    def __init__(self, parent, dmx=None, channels=16, encoder_display=None):
        super().__init__(parent)
        self.dmx = dmx
        self.encoder_display = encoder_display
        self.sliders = []
        self.selected_channel = 1
        self.edit_mode = False

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
        self.update_display()

    def next_channel(self):
        if self.selected_channel < len(self.sliders):
            self.selected_channel += 1
        self.update_display()

    def previous_channel(self):
        if self.selected_channel > 1:
            self.selected_channel -= 1
        self.update_display()

    def toggle_edit_mode(self):
        self.edit_mode = not self.edit_mode
        self.update_display()

    def update_display(self):
        if self.encoder_display:
            value = self.sliders[self.selected_channel - 1][1].get()
            self.encoder_display.update(self.selected_channel, value, self.edit_mode)

    def set_selected(self, channel):
        if 1 <= channel <= len(self.sliders):
            self.selected_channel = channel
            self.update_display()
