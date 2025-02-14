from pygame import time

from config import *



class menu():
    def __init__(self):
        self.img = pygame.image.load('buildings/image/barony.png')
        self.menudraw = pygame.image.load('buildings/image/menu.png')
        self.play = GoldenButton(sc, (64*9, 64*10), "Play", DARKBLUE)
        self.exit = GoldenButton(sc, (64*9, 64*11), "Exit", DARKGREEN)
        self.true = False
        self.lul = choosemenu()
    def use(self, event):
        if self.true:
            return self.lul.use(event)
        else:
            if self.play.update(event):
                self.true = True
                self.lul.runtime(time.get_ticks())
            if self.exit.update(event):
                const.run = False
    def draw(self):
        sc.blit(self.menudraw, (0, 0))
        sc.blit(self.img, (64 * 5 + 52, 0))
        if self.true:
            self.lul.draw()
        else:
            self.play.draw()
            self.exit.draw()

class choosemenu():
    def __init__(self):
        self.play_new= GoldenButton(sc, (64*9-16, 64*10), "Newgame ", LIGHTGRAY)
        self.load = GoldenButton(sc, (64*9, 64*11), "Load", LIGHTGRAY)
        self.time = 0
        self.difficulty_choose = False
        self.easy = GoldenButton(sc, (64*9, 64*10), "Easy", LIGHTGRAY)
        self.normal = GoldenButton(sc, (64*9-16, 64*11), "Normal ", LIGHTGRAY)
        self.hard = GoldenButton(sc, (64*9, 64*12), "Hard", LIGHTGRAY)
    def use(self, event):
        nowtime = time.get_ticks()
        if self.time != 0 and nowtime > self.time + 2000:
            if self.play_new.update(event):
                self.difficulty_choose = True
                self.time = nowtime
            if self.load.update(event):
                tf[0] = False
                tf[2] = True
            if self.difficulty_choose:
                if self.easy.update(event):
                    self.lulwa()
                    return "EASY"
                if self.normal.update(event):
                    self.lulwa()
                    return "NORMAL"
                if self.hard.update(event):
                    self.lulwa()
                    return "HARD"
    def draw(self):
        if self.difficulty_choose:
            self.easy.draw()
            self.normal.draw()
            self.hard.draw()
        else:
            self.play_new.draw()
            self.load.draw()
    def runtime(self, timee):
        self.time = timee
    def lulwa(self):
        tf[0] = False
        tf[2] = True

class exitmenu():
    def __init__(self):
        self.savebutton = TextButton(sc, (1152 / 4, 400), "Yes", LIGHTGREEN)
        self.nosavebutton = TextButton(sc, (1152 / 4 + 100, 400), "No", LIGHTRED)
    def use(self, event):
        return (self.savebutton.update(event),self.nosavebutton.update(event))
    def draw(self):
        self.savebutton.draw()
        self.nosavebutton.draw()



