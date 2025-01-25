import tkinter as tk
from tkinter import messagebox
from service.game_service import CharacterService
from application.game_setup import setup_game

class GameUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Pet Game")

        # Setup awal game
        self.character_service = None
        self.character = None

        self.setup_ui()

    def setup_ui(self):
        # Tombol untuk memulai permainan
        self.start_button = tk.Button(self.root, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=10)

        # Label untuk status karakter
        self.status_label = tk.Label(self.root, text="Character Status: Waiting to start game", font=("Arial", 12))
        self.status_label.pack(pady=20)

        # Tombol untuk memberi makan
        self.feed_button = tk.Button(self.root, text="Feed Pet", state="disabled", command=self.feed_pet)
        self.feed_button.pack(pady=5)

        # Tombol untuk bermain
        self.play_button = tk.Button(self.root, text="Play with Pet", state="disabled", command=self.play_with_pet)
        self.play_button.pack(pady=5)

        # Tombol untuk beristirahat
        self.rest_button = tk.Button(self.root, text="Rest Pet", state="disabled", command=self.rest_pet)
        self.rest_button.pack(pady=5)

    def start_game(self):
        """Start the game and setup character"""
        self.character = setup_game()
        self.character_service = CharacterService(self.character.name)
        
        # Enable action buttons after the game is set up
        self.feed_button.config(state="normal")
        self.play_button.config(state="normal")
        self.rest_button.config(state="normal")

        self.update_status()

    def feed_pet(self):
        """Feed the pet and update the UI with random amount"""
        status = self.character_service.feed_character()
        self.update_status(status)

    def play_with_pet(self):
        """Play with the pet and update the UI with random play time"""
        status = self.character_service.play_with_character()
        self.update_status(status)

    def rest_pet(self):
        """Rest the pet and update the UI with random rest time"""
        status = self.character_service.rest_character()
        self.update_status(status)

    def update_status(self, status=None):
        """Update the status label"""
        if not status:
            status = self.character_service._get_character_status()
        
        status_text = f"Name: {status['name']}\n" \
                      f"Hunger Level: {status['hunger_level']}\n" \
                      f"Happiness Level: {status['happiness_level']}\n" \
                      f"Energy Level: {status['energy_level']}"
        self.status_label.config(text=status_text)


def main():
    root = tk.Tk()
    game_ui = GameUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
