class Character:
    def __init__(self, name, health, hunger_level=0, happiness_level=100):
        self.name = name
        self.health_level = health
        self.hunger_level = hunger_level
        self.happiness_level = happiness_level

    def feed(self, amount):
        # Mengurangi hunger_level sesuai dengan jumlah yang diberikan, memastikan tidak kurang dari 0
        self.hunger_level = max(0, self.hunger_level - amount)
        
        # Meningkatkan happiness_level, tetapi tidak melebihi 100
        self.happiness_level = min(100, self.happiness_level + amount)

        # Menampilkan status setelah diberi makan
        print(f"{self.name} has been fed! Hunger level: {self.hunger_level}, Happiness level: {self.happiness_level}")
