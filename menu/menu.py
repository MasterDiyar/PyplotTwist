from config import *

class menu():
    def __init__(self):
        self.play = Button(GREEN, sc, 64, 64, 128, 64)
        self.exit = Button(RED, sc, 64, 144, 128, 64)
    def use(self, event):
        if self.play.update(event):
            tf[0] = False
            tf[1] = True
        if self.exit.update(event):
            run = False
    def draw(self):
        self.play.draw()
        self.exit.draw()

