import buildings
from config import *

def difficulty(type):
    if type == "":

class Game:
    def __init__(self):
        self.atlas = buildings.ClickMap(sc, "saves/firstmap.txt")
        self.week = 1
        self.week_button = TextButton(sc, (900, 640), "NEXT WEEK", LIGHTGRAY)
        self.resources = {"stone:": 0, "wheat:": 0, "heads:": 0, "population:": 0, }