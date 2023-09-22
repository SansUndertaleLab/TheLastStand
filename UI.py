from pygame import font

font.init()

class UI:
    def __init__(self):
        self.elements = []
        self.click_pos = None

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
    
    def update_buttons(self):
        for i in self.elements:
            if isinstance(i, Button):
                clicked =  (self.click_pos is not None) and i.check_overlap(self.click_pos)
                if clicked:
                    if not i.debounce:
                        i.clicked()
                    i.debounce = True
                else:
                    i.debounce = False
        self.click_pos = None

    def clicked(self, position):
        self.click_pos = position

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

    def get_size(self):
        return font.Font.size(self.font, self.text)

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
    
class Button(Label):
    def __init__(self, position, display, text, font, color = (255, 255, 255)):
        super().__init__(position, display, text, font, color)
        self.subscribed_functions = []
        self.debounce = False

    def subscribe(self, function):
        if function not in self.subscribed_functions:
            self.subscribed_functions.append(function)
        return self
    
    def unsubscribe(self, function):
        for i, v in enumerate(self.subscribed_functions):
            if v is function:
                self.subscribed_functions.pop(i)

    def clicked(self):
        for i in self.subscribed_functions:
            i()

    def check_overlap(self, position):
        size = self.get_size()
        borders = [*self.position, *(self.position[0] + size[0], self.position[1] + size[1])]

        if position[0] > borders[0] and position[0] < borders[2] and position[1] > borders[1] and position[1] < borders[3]:
            return True
        return False