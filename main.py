import tkinter as tk

from gui import OpenDMXStudioGUI
from controllers.arduino_controller import ArduinoController


if __name__ == "__main__":
    root = tk.Tk()

    app = OpenDMXStudioGUI(root)

    # Start Arduino controller
    arduino = ArduinoController(app)
    app.arduino = arduino

    root.mainloop()
