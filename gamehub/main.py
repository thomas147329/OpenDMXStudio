import json
import os
import subprocess
import sys
import tkinter as tk
from tkinter import messagebox

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GAMES_FILE = os.path.join(BASE_DIR, "games.json")

BG = "#111318"
PANEL = "#191c22"
CARD = "#20242c"
TEXT = "#f5f7fa"
MUTED = "#9aa3b2"
ACCENT = "#66c0f4"


class GameHub(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GameHub")
        self.geometry("1050x700")
        self.minsize(850, 560)
        self.configure(bg=BG)

        self.games = self.load_games()
        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", lambda *_: self.refresh_games())

        self.build_ui()
        self.refresh_games()

    def load_games(self):
        try:
            with open(GAMES_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except (OSError, json.JSONDecodeError) as exc:
            messagebox.showerror("GameHub", f"Could not load games.json:\n{exc}")
            return []

    def build_ui(self):
        sidebar = tk.Frame(self, bg=PANEL, width=220)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        logo = tk.Label(
            sidebar,
            text="🎮 GameHub",
            bg=PANEL,
            fg=TEXT,
            font=("Helvetica", 22, "bold"),
            pady=28,
        )
        logo.pack(fill="x")

        self.nav_button(sidebar, "⌂  Home", True)
        self.nav_button(sidebar, "▣  Library")
        self.nav_button(sidebar, "★  Favorites")
        self.nav_button(sidebar, "⚙  Settings")

        tk.Label(
            sidebar,
            text="YOUR GAMES",
            bg=PANEL,
            fg=MUTED,
            font=("Helvetica", 9, "bold"),
            anchor="w",
            padx=20,
            pady=18,
        ).pack(fill="x")

        self.sidebar_games = tk.Frame(sidebar, bg=PANEL)
        self.sidebar_games.pack(fill="x")

        content = tk.Frame(self, bg=BG)
        content.pack(side="right", fill="both", expand=True)

        top = tk.Frame(content, bg=BG, height=76)
        top.pack(fill="x", padx=28, pady=(18, 0))
        top.pack_propagate(False)

        tk.Label(
            top,
            text="Home",
            bg=BG,
            fg=TEXT,
            font=("Helvetica", 25, "bold"),
        ).pack(side="left", pady=12)

        search = tk.Entry(
            top,
            textvariable=self.search_var,
            bg=PANEL,
            fg=TEXT,
            insertbackground=TEXT,
            relief="flat",
            font=("Helvetica", 12),
        )
        search.pack(side="right", ipadx=12, ipady=9, padx=(20, 0), pady=12)
        search.insert(0, "")

        tk.Label(
            content,
            text="Featured Games",
            bg=BG,
            fg=TEXT,
            font=("Helvetica", 18, "bold"),
            anchor="w",
        ).pack(fill="x", padx=28, pady=(8, 14))

        self.canvas = tk.Canvas(content, bg=BG, highlightthickness=0)
        scrollbar = tk.Scrollbar(content, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True, padx=(28, 0))

        self.game_frame = tk.Frame(self.canvas, bg=BG)
        self.canvas_window = self.canvas.create_window((0, 0), window=self.game_frame, anchor="nw")
        self.game_frame.bind("<Configure>", self.update_scroll_region)
        self.canvas.bind("<Configure>", self.resize_game_frame)

    def nav_button(self, parent, text, active=False):
        button = tk.Button(
            parent,
            text=text,
            command=lambda: None,
            bg="#252a33" if active else PANEL,
            fg=TEXT if active else MUTED,
            activebackground="#2c323d",
            activeforeground=TEXT,
            relief="flat",
            bd=0,
            anchor="w",
            padx=20,
            font=("Helvetica", 12, "bold"),
        )
        button.pack(fill="x", padx=10, pady=3, ipady=8)

    def update_scroll_region(self, _event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def resize_game_frame(self, event):
        self.canvas.itemconfigure(self.canvas_window, width=event.width)

    def refresh_games(self):
        for widget in self.game_frame.winfo_children():
            widget.destroy()
        for widget in self.sidebar_games.winfo_children():
            widget.destroy()

        query = self.search_var.get().strip().lower()
        visible = [
            game for game in self.games
            if query in game["name"].lower() or query in game.get("description", "").lower()
        ]

        for game in self.games:
            if not query or game in visible:
                tk.Label(
                    self.sidebar_games,
                    text=game["name"],
                    bg=PANEL,
                    fg=MUTED,
                    anchor="w",
                    padx=30,
                    pady=6,
                    font=("Helvetica", 10),
                ).pack(fill="x")

        columns = 2
        for index, game in enumerate(visible):
            row, column = divmod(index, columns)
            card = self.create_card(self.game_frame, game)
            card.grid(row=row, column=column, sticky="nsew", padx=(0, 14), pady=(0, 14))

        for column in range(columns):
            self.game_frame.grid_columnconfigure(column, weight=1)

        self.after(50, self.update_scroll_region)

    def create_card(self, parent, game):
        card = tk.Frame(parent, bg=CARD, padx=16, pady=16)

        art = tk.Label(
            card,
            text=game.get("icon", "🎮"),
            bg="#292f39",
            fg=TEXT,
            font=("Helvetica", 42),
            height=2,
        )
        art.pack(fill="x")

        tk.Label(
            card,
            text=game["name"],
            bg=CARD,
            fg=TEXT,
            font=("Helvetica", 15, "bold"),
            anchor="w",
        ).pack(fill="x", pady=(12, 4))

        tk.Label(
            card,
            text=game.get("description", ""),
            bg=CARD,
            fg=MUTED,
            font=("Helvetica", 10),
            anchor="w",
            justify="left",
            wraplength=360,
        ).pack(fill="x")

        bottom = tk.Frame(card, bg=CARD)
        bottom.pack(fill="x", pady=(14, 0))

        tk.Label(
            bottom,
            text=game.get("genre", "Game"),
            bg=CARD,
            fg=MUTED,
            font=("Helvetica", 9),
        ).pack(side="left")

        tk.Button(
            bottom,
            text="PLAY",
            command=lambda g=game: self.launch_game(g),
            bg=ACCENT,
            fg="#101318",
            activebackground="#8bd2fa",
            relief="flat",
            font=("Helvetica", 10, "bold"),
            padx=16,
            pady=6,
        ).pack(side="right")

        return card

    def launch_game(self, game):
        path = os.path.join(BASE_DIR, game["path"])
        if not os.path.isfile(path):
            messagebox.showerror("GameHub", f"Game file not found:\n{path}")
            return

        try:
            subprocess.Popen([sys.executable, path], cwd=os.path.dirname(path))
        except OSError as exc:
            messagebox.showerror("GameHub", f"Could not start {game['name']}:\n{exc}")


if __name__ == "__main__":
    GameHub().mainloop()
