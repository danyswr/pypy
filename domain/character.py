class Character:
    def __init__(self, name, species, age, hunger_level=0, happiness_level=100):
        self.name = name
        self.species = species
        self.age = age
        self.hunger_level = hunger_level
        self.happiness_level = happiness_level

    def feed(self, amount):
        """
        Feeds the character, decreasing the hunger level.
        """
        self.hunger_level = max(0, self.hunger_level - amount)
        self.happiness_level = min(100, self