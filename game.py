from pygments.lexers import diff

import buildings
from buildings import InfoMap
from config import *
import config.Decoder as dec
import buildings.blueprint as blp
import Techtree



def difficulty(type):
    if type == "EASY":
        return {"money:": 3000, "wheat:": 200, "heads:": 50, "population:": 400, "wood:":200, "coal:":30, "warior:":1}
    if type == "NORMAL":
        return {"money:": 1000, "wheat:": 200, "heads:": 45, "population:": 400, "wood:":200, "coal:":30, "warior:":1}
    if type == "HARD":
        return {"money:": 500, "wheat:": 100, "heads:": 40, "population:": 400, "wood:":200, "coal:":30, "warior:":0}

class Game:
    def __init__(self, diff):
        self.bg = pygame.image.load("buildings/image/backendl.png")
        self.atlas = buildings.Map(sc, "saves/firstmap.txt")
        self.mapinfo = []
        self.week = 1
        self.resources = difficulty(diff)
        self.surface = pygame.Surface((1152, 768), pygame.SRCALPHA)
        self.upgrade_tab = False
        self.updatemap()
        self.draft = blp.Building()
        self.house_maps = InfoMap(self.surface, "saves/firstmap.txt", self.mapinfo)
        self.week_button = GoldenButton(self.surface, (900, 640), "NEXT WEEK    ", LIGHTGRAY)
        self.difficulty = diff
        self.treep = NewTree(diff, None)

    def update(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.upgrade_tab = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not self.upgrade_tab:
            pos = (event.pos[0]//64-2, event.pos[1]//64-1)
            if 0 <= pos[0] <= 12 and 0 <= pos[1] <= 7:
                self.upgrade_tab = True
                self.draft.clear()
                self.draft.reader(pos)
                self.treep = NewTree(diff, dec.tiledecode(int(dec.gettilefromtextpos(pos))))
                self.treep.tree.resources=self.resources
            if self.week_button.update(event):
                self.week_calculation()
        if self.upgrade_tab and event.type == pygame.MOUSEBUTTONDOWN:
            self.treep.update(event.pos)

    def draw(self):
        self.surface.blit(self.bg, (0, 0))
        i = 0
        for text, count in self.resources.items():
            drawtext(self.surface, (text+" "+str(count)), (10+100*i, 20), BLACK)
            i += 1
        if self.upgrade_tab:
            self.draft.draw(self.surface)
            self.treep.draw(self.surface)
        else:
            self.atlas.draw(self.surface)
            self.house_maps.draw(self.surface)
            self.week_button.draw()


        sc.blit(self.surface, (0, 0))

    def updatemap(self):
        with open("saves/firstmap.info", "r") as f:
            for line in f.readlines():
                a = line.split()[:-1]
                a.append((line.split(" ")[-1])[0:2])
                self.mapinfo.append(a)

    def week_calculation(self):
        self.week += 1
        pap = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0}
        building = {"00":0, "AA":0, "A1":0, "A2":0,"A3":0, "A4":0,"A5":0, "C1":0,"C2":0, "C3":0}
        with open("saves/firstmap.txt", "r") as line:
            all = line.readlines()
            for l in all:
                for j in l.split():
                    pap[j] += 1
        with open("saves/firstmap.info", "r") as line:
            all = line.readlines()
            for l in all:
                for j in l.split():
                    for fr in range(0, len(j), 2):
                        key = j[fr:fr + 2]
                        if key not in building:
                            building[key] = 0
                        building[key] += 1
        money = self.resources["money:"]
        wheat = self.resources["wheat:"]
        heads = self.resources["heads:"]
        population = self.resources["population:"]
        wood = self.resources["wood:"]
        coal = self.resources["coal:"]
        warior = self.resources["warior:"]

        #give
        money += pap["3"]*5 if self.difficulty == "EASY" else pap["3"]*4
        money += pap["1"] + pap["2"]*2
        wheat += pap["1"]*2 + pap["2"]*4 + heads//6
        population += 1
        heads += heads//20
        wood += population//10
        coal += population//20

        #take
        money -= warior*5
        wheat -= warior*2 + heads//4 + population//3

        self.resources["money:"] = money
        self.resources["wheat:"] = wheat
        self.resources["heads:"] = heads
        self.resources["population:"] = population
        self.resources["wood:"] = wood
        self.resources["coal:"] = coal
        self.resources["warior:"] = warior
        if self.week == 28:
            tf[2] = False
            tf[3] = True
            with open("saves/final.txt", "w") as f:
                f.write(str(self.resources["money:"]))

class NewTree:
    def __init__(self, diff, typex):
        self.tree = Techtree.TechTree(difficulty(diff))

        self.typeinit(typex)
    def typeinit(self, yup):
        match yup:
            case "GRASS":
                self.tree.add_tech("FARMLAND", 700, 50, cost={"money:":100, "wood:":2, "wheat:":10})
                self.tree.add_tech("MILL", 700, 150, ["FARMLAND"],{"money:":200, "wood:":20})
                self.tree.add_tech("IRRIGATION", 900, 250, ["MILL"],{"money:":350, "wood:":30})
                self.tree.add_tech("BETTER EQUIP", 700, 250, ["MILL"],{"money:":400, "wood:":30})
            case "DESERT":
                self.tree.add_tech("CULTIVATION", 700, 50, cost={"money:":150, "wheat:":10})
                self.tree.add_tech("HARVEST", 700, 150, ["CULTIVATION"],{"money:":150, "wheat:":10})
    def draw(self, screen):
        self.tree.draw(screen)
    def update(self, pos):
        self.tree.handle_click(pos)

