import tkinter as tk
import random
from tkinter import simpledialog, messagebox

# Character Class
class Character:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.physical = random.randint(5, 100)
        self.defense = random.randint(5, 10)

    def attack(self, enemy):
        damage = max(self.physical - enemy.defense, 0)
        enemy.hp -= damage
        return damage

    def is_alive(self):
        return self.hp > 0

# Initialize Characters
def setup_game():
    global player, enemy, player_hp_label, enemy_hp_label, result_label
    player_name = simpledialog.askstring("Input", "Enter your hero's name:")
    enemy_name = simpledialog.askstring("Input", "Enter the enemy's name:")

    if not player_name or not enemy_name:
        messagebox.showerror("Error", "Both names must be entered!")
        root.destroy()
        return

    player = Character(player_name)
    enemy = Character(enemy_name)

    # Update UI
    player_hp_label.config(text=f"{player.name} HP: {player.hp}")
    enemy_hp_label.config(text=f"{enemy.name} HP: {enemy.hp}")
    result_label.config(text="Game started! Choose your action.")

# Attack Action
def attack_enemy():
    if not player.is_alive() or not enemy.is_alive():
        result_label.config(text="Game over. Restart to play again.")
        return

    player_damage = player.attack(enemy)
    update_status(f"{player.name} attacks {enemy.name} for {player_damage} damage!")

    if not enemy.is_alive():
        update_status(f"{enemy.name} is defeated! {player.name} wins!", is_game_over=True)
        return

    enemy_damage = enemy.attack(player)
    update_status(f"{enemy.name} attacks {player.name} for {enemy_damage} damage!")

    if not player.is_alive():
        update_status(f"{player.name} is defeated! {enemy.name} wins!", is_game_over=True)

# Defend Action
def defend_enemy():
    if not player.is_alive() or not enemy.is_alive():
        result_label.config(text="Game over. Restart to play again.")
        return

    damage_reduced = min(enemy.physical, player.defense)
    player.hp -= max(enemy.physical - player.defense, 0)

    update_status(f"{player.name} defends, reducing damage by {damage_reduced}!")
    if not player.is_alive():
        update_status(f"{player.name} is defeated! {enemy.name} wins!", is_game_over=True)
    else:
        enemy_damage = enemy.attack(player)
        update_status(f"{enemy.name} counterattacks for {enemy_damage} damage!")

# Update UI
def update_status(message, is_game_over=False):
    player_hp_label.config(text=f"{player.name} HP: {max(player.hp, 0)}")
    enemy_hp_label.config(text=f"{enemy.name} HP: {max(enemy.hp, 0)}")
    result_label.config(text=message)

    if is_game_over:
        attack_button.config(state="disabled")
        defend_button.config(state="disabled")

# Restart Game
def restart_game():
    setup_game()
    attack_button.config(state="normal")
    defend_button.config(state="normal")

# GUI Setup
root = tk.Tk()
root.title("Virtual Pet Game")
root.geometry("400x300")

# Labels
player_hp_label = tk.Label(root, text="", font=("Arial", 12))
player_hp_label.pack()

enemy_hp_label = tk.Label(root, text="", font=("Arial", 12))
enemy_hp_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Buttons
attack_button = tk.Button(root, text="Attack", font=("Arial", 12), command=attack_enemy)
attack_button.pack(pady=5)

defend_button = tk.Button(root, text="Defend", font=("Arial", 12), command=defend_enemy)
defend_button.pack(pady=5)

restart_button = tk.Button(root, text="Restart", font=("Arial", 12), command=restart_game)
restart_button.pack(pady=5)

# Initialize Game
setup_game()

# Start GUI
root.mainloop()
