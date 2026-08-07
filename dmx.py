class DMXController:
    def __init__(self):
        self.channels = [0] * 512

    def set_channel(self, channel, value):
        if 1 <= channel <= 512:
            self.channels[channel - 1] = max(0, min(255, value))

    def get_channel(self, channel):
        return self.channels[channel - 1]
