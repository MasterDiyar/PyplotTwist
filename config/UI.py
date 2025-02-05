from .const import *

class UIX:
    def __init__(self):
        self.things = []
    def draw(self, screen):
        for i in self.things:
            screen.blit(i, i.getpos())
            i.udpate()
    def add_thing(self, thing):
        self.things.append(thing)
    def remove_thing(self, thing):
        self.things.remove(thing)
        
