from domain.character import Character

class CharacterService:
    def __init__(self, name):
        # Inisialisasi objek karakter dengan nama yang diberikan
        self.character = Character(name)

    def feed_character(self, food_amount):
        """
        Memberi makan karakter, mengurangi tingkat lapar, menambah kebahagiaan, dan energi.
        """
        self.character.feed(food_amount)
        return self._get_character_status()

    def play_with_character(self, play_time):
        """
        Bermain dengan karakter, meningkatkan kebahagiaan dan mengurangi energi.
        """
        self.character.play(play_time)
        return self._get_character_status()

    def rest_character(self, rest_time):
        """
        Istirahatkan karakter, menambah energi, meningkatkan kebahagiaan, dan meningkatkan rasa lapar.
        """
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
