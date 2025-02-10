from config import *

class menu():
    def __init__(self):
        self.play = Button(GREEN, sc, 64, 64, 128, 64)
        self.exit = Button(RED, sc, 64, 144, 128, 64)
    def use(self):
        if self.play.update():
            tf[0] = False
            tf[1] = True
        if self.exit.update():
            run = False

