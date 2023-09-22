from pygame import font

font.init()

class UI:
    def __init__(self):
        self.elements = []

    def render(self):
        for i in self.elements:
            i.render()

    def addElement(self, element):
        self.elements.append(element)

    def get_id(self, element):
        for i, v in enumerate(self.elements):
            if element is v:
                return i
        return None

class UIElement:
    def __init__(self, position, display):
        self.position = position
        self.display = display

    def render(self):
        raise NotImplementedError("Custom render function for UI not available")
    
    def transition(self, new_position, tween):
        pass

class Label(UIElement):
    def __init__(self, position, display, text, font, color = (255, 255, 255)):
        super().__init__(position, display)
        self.text = text
        self.font = font
        self.color = color

    def center_X(self):
        size = font.Font.size(self.font, self.text)[0]
        self.position = (self.display.get_width() // 2 - size // 2, self.position[1])
        return self

    def center_Y(self):
        size = font.Font.size(self.font, self.text)[1]
        self.position = (self.position[0], self.display.get_height() // 2 - size // 2)
        return self

    def center(self):
        size = font.Font.size(self.font, self.text)
        self.position = (self.display.get_width() // 2 - size[0] // 2, self.display.get_height() // 2 - size[1] // 2)
        return self
    
    def centered_X(self):
        size = font.Font.size(self.font, self.text)[1]
        return (self.position[0], self.display.get_height() // 2 - size // 2)

    def centered_Y(self):
        size = font.Font.size(self.font, self.text)[1]
        return (self.position[0], self.display.get_height() // 2 - size // 2)

    def centered(self):
        size = font.Font.size(self.font, self.text)
        return (self.display.get_width() // 2 - size[0] // 2, self.display.get_height() // 2 - size[1] // 2)

    def render(self):
        current_render = self.font.render(self.text, True, self.color)
        self.display.blit(current_render, self.position)
        return self