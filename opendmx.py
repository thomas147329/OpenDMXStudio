class OpenDMX:
    def __init__(self):
        self.channels = [0] * 512
        self.connected = False

    def set_channel(self, channel, value):
        if 1 <= channel <= 512:
            self.channels[channel - 1] = max(0, min(255, value))

    def get_channel(self, channel):
        if 1 <= channel <= 512:
            return self.channels[channel - 1]
        return 0

    def send(self):
        # DMX USB transmission will be added here
        pass
