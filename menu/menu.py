from config import *

class menu():
    def __init__(self):
        self.play = TextButton(sc, (64, 64), "Play", LIGHTBLUE)
        self.exit = TextButton(sc, (64, 144), "Exit", LIGHTRED)
    def use(self, event):
        if self.play.update(event):
            tf[0] = False
            tf[1] = True
        if self.exit.update(event):
            run = False
    def draw(self):
        self.play.draw()
        self.exit.draw()

class choosemenu():
    def __init__(self):
        self.play_new= TextButton(sc, (164, 64), "Newgame", LIGHTGRAY)
        self.load = TextButton(sc, (164, 128), "Load", LIGHTGRAY)
    def use(self, event):
        if self.play_new.update(event):
            tf[1] = False
            tf[2] = True
        if self.load.update(event):
            tf[1] = False
            tf[2] = True
    def draw(self):
        self.play_new.draw()
        self.load.draw()

class exitmenu():
    def __init__(self):
        self.savebutton = TextButton(sc, (1152 / 4, 400), "Yes", LIGHTGREEN)
        self.nosavebutton = TextButton(sc, (1152 / 4 + 100, 400), "No", LIGHTRED)
    def use(self, event):
        return (self.savebutton.update(event),self.nosavebutton.update(event))
    def draw(self):
        self.savebutton.draw()
        self.nosavebutton.draw()



