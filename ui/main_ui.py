import tkinter as tk
from service.game_service import attack, defend
from application.game_setup import setup_game

class GameUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Pet Game")
        self.root.geometry("400x300")

        self.player = None
        self.enemy = None

        self.player_hp_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.player_hp_label.pack()

        self.enemy_hp_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.enemy_hp_label.pack()

        self.result_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        self.attack_button = tk.Button(self.root, text="Attack", font=("Arial", 12), command=self.attack_enemy)
        self.attack_button.pack(pady=5)

        self.defend_button = tk.Button(self.root, text="Defend", font=("Arial", 12), command=self.defend_enemy)
        self.defend_button.pack(pady=5)

        self.restart_button = tk.Button(self.root, text="Restart", font=("Arial", 12), command=self.restart_game)
        self.restart_button.pack(pady=5)

        self.restart_game()

    def update_status(self, message, is_game_over=False):
        self.player_hp_label.config(text=f"{self.player.name} HP: {max(self.player.hp, 0)}")
        self.enemy_hp_label.config(text=f"{self.enemy.name} HP: {max(self.enemy.hp, 0)}")
        self.result_label.config(text=message)

        if is_game_over:
            self.attack_button.config(state="disabled")
            self.defend_button.config(state="disabled")

    def attack_enemy(self):
        if not self.player.is_alive() or not self.enemy.is_alive():
            self.result_label.config(text="Game over. Restart to play again.")
            return

        player_damage, enemy_defeated = attack(self.player, self.enemy)
        self.update_status(f"{self.player.name} attacks {self.enemy.name} for {player_damage} damage!")

        if enemy_defeated:
            self.update_status(f"{self.enemy.name} is defeated! {self.player.name} wins!", is_game_over=True)
            return

        enemy_damage, player_defeated = attack(self.enemy, self.player)
        self.update_status(f"{self.enemy.name} attacks {self.player.name} for {enemy_damage} damage!")

        if player_defeated:
            self.update_status(f"{self.player.name} is defeated! {self.enemy.name} wins!", is_game_over=True)

    def defend_enemy(self):
        if not self.player.is_alive() or not self.enemy.is_alive():
            self.result_label.config(text="Game over. Restart to play again.")
            return

        damage_reduced, player_defeated = defend(self.player, self.enemy)
        self.update_status(f"{self.player.name} defends, reducing damage by {damage_reduced}!")

        if player_defeated:
            self.update_status(f"{self.player.name} is defeated! {self.enemy.name} wins!", is_game_over=True)
            return

        enemy_damage, player_defeated = attack(self.enemy, self.player)
        self.update_status(f"{self.enemy.name} counterattacks for {enemy_damage} damage!")

        if player_defeated:
            self.update_status(f"{self.player.name} is defeated! {self.enemy.name} wins!", is_game_over=True)

    def restart_game(self):
        self.player, self.enemy = setup_game()
        if not self.player or not self.enemy:
            self.root.destroy()
            return

        self.player_hp_label.config(text=f"{self.player.name} HP: {self.player.hp}")
        self.enemy_hp_label.config(text=f"{self.enemy.name} HP: {self.enemy.hp}")
        self.result_label.config(text="Game started! Choose your action.")
        self.attack_button.config(state="normal")
        self.defend_button.config(state="normal")