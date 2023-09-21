class Entity:
    def __init__(self):
        self.health = 100
        self.active = True
        self.position = (0, 0)
        self.sprite = None
        
    def damage(self, damage):
        self.health -= damage

        if self.health <= 0:
            self.die()

    def die(self):
        self.active = False

    def render(self, display):
        display.blit(self.sprite, self.position)

    def set_sprite(self, sprite):
        self.sprite = sprite