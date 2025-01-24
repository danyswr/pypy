from tkinter import simpledialog, messagebox
from domain.character import Character

def setup_game():
    player_name = simpledialog.askstring("Input", "Enter your hero's name:")
    enemy_name = simpledialog.askstring("Input", "Enter the enemy's name:")

    if not player_name or not enemy_name:
        messagebox.showerror("Error", "Both names must be entered!")
        return None, None

    player = Character(player_name)
    enemy = Character(enemy_name)

    return player, enemy
