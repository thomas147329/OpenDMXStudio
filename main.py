import tkinter as tk
from gui import OpenDMXStudioGUI


if __name__ == "__main__":
    root = tk.Tk()
    app = OpenDMXStudioGUI(root)
    root.mainloop()
