## single entry point app

from ui.main_ui import GameUI
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    game_ui = GameUI(root)
    root.mainloop()

