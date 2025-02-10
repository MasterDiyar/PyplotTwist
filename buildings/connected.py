import pygame
from config.const import *
from .blueprint import *

class Map:
    def __init__(self, surface, mapinfo):
        self.map = []
        self.surface = surface
        self.full_tilemap = pygame.image.load("buildings/image/tilemap.png").convert_alpha()
        with open(mapinfo, "r") as line:
            all = line.readlines()
            for l in all:
                self.map.append(l.split())
    def draw(self):
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
        return map
    

class ClickMap(Map):
    def __init__(self, surface, mapinfo):
        super().__init__(surface, mapinfo)
        self.starttime = pygame.time.get_ticks()
        self.clicked = False
        self.bp = Building()
        self.newpos = (0,0)
    def update(self):
        keys = pygame.key.get_pressed()
        time = pygame.time.get_ticks()
        mouse = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and time - self.starttime >= 2000:
            self.bp.clear()
            self.newpos = (mouse[0]//64 - map_margin[0]//64, mouse[1]//64 - map_margin[1]//64)
            self.clicked = True
        if self.clicked:
            self.bp.draw(self.surface)
            self.bp.reader(self.newpos)
        if keys[pygame.K_ESCAPE]:
            self.clicked = False

    def getpos(self):
        return (0, 0)




        