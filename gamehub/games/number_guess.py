import random
import tkinter as tk
from tkinter import messagebox


def main():
    root = tk.Tk()
    root.title("Number Guess")
    root.geometry("420x300")
    root.configure(bg="#111318")

    target = random.randint(1, 100)
    attempts = 0

    tk.Label(root, text="🔢 Number Guess", bg="#111318", fg="white", font=("Helvetica", 22, "bold")).pack(pady=25)
    tk.Label(root, text="Guess a number from 1 to 100", bg="#111318", fg="#9aa3b2", font=("Helvetica", 12)).pack()

    entry = tk.Entry(root, font=("Helvetica", 16), justify="center")
    entry.pack(pady=20)
    entry.focus()

    status = tk.Label(root, text="", bg="#111318", fg="#66c0f4", font=("Helvetica", 12, "bold"))
    status.pack(pady=5)

    def guess():
        nonlocal attempts
        try:
            value = int(entry.get())
        except ValueError:
            status.config(text="Enter a whole number.")
            return

        attempts += 1
        if value < target:
            status.config(text="Too low!")
        elif value > target:
            status.config(text="Too high!")
        else:
            messagebox.showinfo("You win!", f"You found it in {attempts} guesses!")
            root.destroy()

    tk.Button(root, text="GUESS", command=guess, bg="#66c0f4", fg="#101318", relief="flat", font=("Helvetica", 11, "bold"), padx=20, pady=8).pack()
    root.bind("<Return>", lambda _event: guess())
    root.mainloop()


if __name__ == "__main__":
    main()
