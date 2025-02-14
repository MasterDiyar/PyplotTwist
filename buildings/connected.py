import pygame
from config.const import *
from .blueprint import *
import random

class Map:
    def __init__(self, surface, mapinfo):
        self.map = []
        self.surface = surface
        self.mapinfo = mapinfo
        with open(self.mapinfo, "r") as line:
            all = line.readlines()
            for l in all:
                self.map.append(l.split())
    def draw(self, screen):
        map = pygame.Surface((len(self.map[0]) * 64,len(self.map) * 64))
        
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                match self.map[i][j]:
                    case "1":
                        map.blit(tiles["GRASS"], (j*64, i*64))
                    case "2":
                        map.blit(tiles["FARMLAND"], (j*64, i*64))
                    case "3":
                        map.blit(tiles["WATER"], (j*64, i*64))
                    case "4":
                        map.blit(tiles["FOREST"], (j*64, i*64))
                    case "5":
                        map.blit(tiles["SAVANNA"], (j*64, i*64))
                    case "6":
                        map.blit(tiles["ASHLAND"], (j*64, i*64))
                    case "7":
                        map.blit(tiles["DESERT"], (j*64, i*64))
                    case "8":
                        map.blit(tiles["MOUNTAIN"], (j*64, i*64))
        screen.blit(map, map_margin)
    def update_map(self):
        with open(self.mapinfo, "r") as line:
            all = line.readlines()
            for l in all:
                self.map.append(l.split())

class ClickMap(Map):
    def __init__(self, surface, mapinfo):
        super().__init__(surface, mapinfo)
        self.starttime = pygame.time.get_ticks()
        self.clicked = False
        self.bp = Building()
        self.newpos = (0,0)
        self.nmap=self.bp.nmap
    def update(self):
        keys = pygame.key.get_pressed()
        time = pygame.time.get_ticks()
        mouse = pygame.mouse.get_pos()
        self.nmap = self.bp.nmap
        if pygame.mouse.get_pressed()[0] and time - self.starttime >= 2000:
            self.bp.clear()
            self.newpos = (mouse[0]//64 - map_margin[0]//64, mouse[1]//64 - map_margin[1]//64)
            self.clicked = True
        if self.clicked:
            self.bp.draw(self.surface)
            self.bp.reader(self.newpos)


    def getpos(self):
        return (0, 0)

class InfoMap(Map):
    def __init__(self,surface, mapinfo, decoded):
        super().__init__(surface, mapinfo)
        self.houses = ["HOUSE1", "HOUSE2", "HOUSE3", "HOUSE4", "HOUSE5"]
        self.decoded = decoded
        self.atlas = pygame.Surface((len(self.map[0]) * 64, len(self.map) * 64), pygame.SRCALPHA)
        self.save_draw()
    def save_draw(self):

        for i in range(len(self.decoded)):
            for j in range(len(self.decoded[i])):
                match self.decoded[i][j][:2]:
                    case "00":
                        if self.map[i][j] != "3":
                            self.atlas.blit(pygame.transform.scale_by(houses[self.houses[random.randint(0, 4)]], 2.5), (j*64+random.randint(-16, 16), i*64+random.randint(-16, 16)))
                    case "AA":
                        self.atlas.blit(pygame.transform.scale_by(houses["FARM"], 2.5), (j*64+random.randint(-16, 16), i*64+random.randint(-16, 16)))
                    case "BB":
                        pass
                    case "A1":
                        self.atlas.blit(pygame.transform.scale_by(houses["FARMLAND"], 2.5), (j*64+random.randint(-16, 16), i*64+random.randint(-16, 16)))
                    case "A2", "A4":
                        self.atlas.blit(pygame.transform.scale_by(houses["MILL"], 2.5), (j*64+random.randint(-16, 16), i*64+random.randint(-16, 16)))
                    case "A3":
                        self.atlas.blit(pygame.transform.scale_by(houses["WATERWHEEL"], 2.5), (j*64+random.randint(-16, 16), i*64+random.randint(-16, 16)))
                    case "C1", "C2", "C3":
                        self.atlas.blit(pygame.transform.scale_by(houses["FARMLAND"], 2.5), (j*64+random.randint(-16, 16), i*64+random.randint(-16, 16)))
    def draw(self, surface):
        surface.blit(self.atlas, map_margin)


        