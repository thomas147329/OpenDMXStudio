import serial
import threading

class ArduinoController:
    def __init__(self, port=None, baud=9600):
        self.port = port
        self.baud = baud
        self.serial = None
        self.callback = None

    def connect(self):
        if not self.port:
            return False
        try:
            self.serial = serial.Serial(self.port, self.baud, timeout=1)
            threading.Thread(target=self.listen, daemon=True).start()
            return True
        except Exception as e:
            print("Arduino connection error:", e)
            return False

    def listen(self):
        while self.serial:
            try:
                data = self.serial.readline().decode().strip()
                if data and self.callback:
                    self.callback(data)
            except:
                pass

    def send(self, message):
        if self.serial:
            self.serial.write((message + "\n").encode())
