import random
import tkinter as tk

WIDTH, HEIGHT = 700, 500


def main():
    root = tk.Tk()
    root.title("Space Dodge")
    root.resizable(False, False)

    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#070b14", highlightthickness=0)
    canvas.pack()

    player = canvas.create_polygon(350, 450, 335, 475, 365, 475, fill="#66c0f4", outline="white")
    asteroids = []
    keys = {"Left": False, "Right": False}
    score = 0
    running = True

    score_text = canvas.create_text(20, 20, anchor="nw", fill="white", font=("Helvetica", 16, "bold"), text="Score: 0")
    canvas.create_text(WIDTH // 2, 25, fill="#9aa3b2", font=("Helvetica", 11), text="← → to move")

    def key_down(event):
        if event.keysym in keys:
            keys[event.keysym] = True

    def key_up(event):
        if event.keysym in keys:
            keys[event.keysym] = False

    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    def spawn():
        if running:
            x = random.randint(15, WIDTH - 15)
            size = random.randint(8, 20)
            speed = random.randint(3, 7)
            asteroid = canvas.create_oval(x - size, -size, x + size, size, fill="#d7dbe2", outline="")
            asteroids.append((asteroid, speed, size))
            root.after(random.randint(350, 800), spawn)

    def game_loop():
        nonlocal score, running
        if not running:
            return

        dx = 0
        if keys["Left"]:
            dx -= 8
        if keys["Right"]:
            dx += 8

        canvas.move(player, dx, 0)
        px1, py1, px2, py2 = canvas.bbox(player)
        if px1 < 0:
            canvas.move(player, -px1, 0)
        if px2 > WIDTH:
            canvas.move(player, WIDTH - px2, 0)

        remaining = []
        for asteroid, speed, size in asteroids:
            canvas.move(asteroid, 0, speed)
            box = canvas.bbox(asteroid)
            if box[1] > HEIGHT:
                canvas.delete(asteroid)
                score += 1
                continue

            p = canvas.bbox(player)
            if p[2] > box[0] and p[0] < box[2] and p[3] > box[1] and p[1] < box[3]:
                running = False
                canvas.create_text(WIDTH // 2, HEIGHT // 2 - 20, fill="white", font=("Helvetica", 32, "bold"), text="GAME OVER")
                canvas.create_text(WIDTH // 2, HEIGHT // 2 + 25, fill="#66c0f4", font=("Helvetica", 16), text=f"Score: {score}")
                return
            remaining.append((asteroid, speed, size))

        asteroids[:] = remaining
        canvas.itemconfig(score_text, text=f"Score: {score}")
        root.after(30, game_loop)

    spawn()
    game_loop()
    root.mainloop()


if __name__ == "__main__":
    main()
