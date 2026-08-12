# GameHub

A simple Steam-inspired Python game launcher built with Tkinter.

## Run

From the repository root:

```bash
python3 gamehub/main.py
```

No third-party Python packages are required.

## Adding a game

1. Put the game's Python file in `gamehub/games/`.
2. Add an entry to `gamehub/games.json`.
3. Use a path relative to the `gamehub` folder, such as `games/my_game.py`.
4. Start GameHub again.

GameHub automatically creates a card for every game in `games.json` and launches it as a separate Python process.
