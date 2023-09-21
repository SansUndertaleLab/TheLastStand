from Entity import Entity
# Player super class

class Player(Entity):
    def __init__(self):
        super().__init__()
        self.inventory = []

    
