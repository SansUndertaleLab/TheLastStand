from pickle import dump, load

RoomID = {
    "Beds": 0,
    "Lab": 1,
    "Farm": 2,
    "Graveyard": 3
}

class Room:
    def __init__(self, id):
        self.id = id

class World:
    def __init__(self):
        self.player = None
        self.npcs = []
        self.infection = []
        self.rooms = []

    def render_world(self):
        self.player.render()