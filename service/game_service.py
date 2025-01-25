import random
from domain.character import Character

class CharacterService:
    def __init__(self, name):
        self.character = Character(name)

    def feed_character(self):
        """
        Memberi makan karakter, mengurangi tingkat lapar, menambah kebahagiaan, dan energi.
        Nilai untuk makanan diacak antara 10 dan 50.
        """
        food_amount = random.randint(10, 50)
        self.character.feed(food_amount)
        return self._get_character_status()

    def play_with_character(self):
        """
        Bermain dengan karakter, meningkatkan kebahagiaan dan mengurangi energi.
        Nilai untuk bermain diacak antara 1 dan 5 jam.
        """
        play_time = random.randint(1, 5)
        self.character.play(play_time)
        return self._get_character_status()

    def rest_character(self):
        """
        Istirahatkan karakter, menambah energi, meningkatkan kebahagiaan, dan meningkatkan rasa lapar.
        Nilai untuk istirahat diacak antara 1 dan 3 jam.
        """
        rest_time = random.randint(1, 3)
        self.character.rest(rest_time)
        return self._get_character_status()

    def _get_character_status(self):
        """
        Mengambil status terbaru dari karakter.
        """
        return {
            'name': self.character.name,
            'hunger_level': self.character.hunger_level,
            'happiness_level': self.character.happiness_level,
            'energy_level': self.character.energy_level
        }
