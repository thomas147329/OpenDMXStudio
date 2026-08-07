class ArduinoController:
    def __init__(self, callback=None):
        self.callback = callback
        self.connected = False
        self.port = None

    def connect(self, port):
        self.port = port
        self.connected = True
        return True

    def handle_event(self, event):
        if self.callback:
            self.callback(event)

    def encoder_right(self):
        self.handle_event("ENCODER_RIGHT")

    def encoder_left(self):
        self.handle_event("ENCODER_LEFT")

    def encoder_press(self):
        self.handle_event("ENCODER_PRESS")
