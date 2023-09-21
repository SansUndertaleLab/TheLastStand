from Entity import Entity

# NPC super class

class NPC(Entity):
    def __init__(self):
        super().__init__()
        self.name = None
        self.infected = True
        self.infection_rate = 1.0
        self.accessories = []