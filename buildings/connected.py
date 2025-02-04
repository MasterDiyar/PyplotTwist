import pygame
from config.const import *

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




        