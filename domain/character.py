class Character:
    def __init__(self, name, hunger_level=0, happiness_level=100, energy_level=100):
        self.name = name
        self.hunger_level = hunger_level
        self.happiness_level = happiness_level
        self.energy_level = energy_level

    def feed(self, food_amount):
        self.hunger_level -= food_amount
        if self.hunger_level < 0:
            self.hunger_level = 0
        self.happiness_level += 10
        self.energy_level += 5

    def play(self, play_time):
        self.happiness_level += play_time * 5
        self.energy_level -= play_time * 10

    def rest(self, rest_time):
        self.energy_level += rest_time * 20
        self.hunger_level += rest_time * 2
        self.happiness_level += rest_time * 3
