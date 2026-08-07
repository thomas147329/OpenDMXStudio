class Fixture:
    def __init__(self, name, address, channels=1):
        self.name = name
        self.address = address
        self.channels = channels

    @property
    def dmx_channel(self):
        return self.address

    def set_channel(self, offset, value, universe):
        channel = self.address + offset
        universe.set_channel(channel, value)

    def __str__(self):
        return f"{self.name} @ DMX {self.address}"
