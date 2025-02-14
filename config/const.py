import pygame

sc = pygame.display.set_mode((1152, 768))
run = True

pygame.font.init()
font = pygame.font.SysFont("TimesNewRoman", 15)

map_margin = (128, 64)
DARKBLUE =(18, 58, 112)
DARKGREEN = (18, 58, 112)
GOLDEN = (255,215,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (88, 88, 88)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHTGRAY=(200,200,200)
LIGHTBLUE=(180, 202, 237)
LIGHTRED=(230, 189, 184)
LIGHTGREEN=(230, 189, 184)

full_tilemap = pygame.image.load("buildings/image/tilemap.png").convert_alpha()
house_tilemap = pygame.image.load("buildings/image/house.png").convert_alpha()

tf = [False for _ in range(10)]

tile_rects = {
    "GRASS": pygame.Rect(0, 0, 64, 64),
    "FARMLAND": pygame.Rect(64, 0, 64, 64),
    "WATER": pygame.Rect(128, 0, 64, 64),
    "FOREST": pygame.Rect(192, 0, 64, 64),
    "SAVANNA": pygame.Rect(0, 64, 64, 64),
    "ASHLAND": pygame.Rect(64, 64, 64, 64),
    "DESERT": pygame.Rect(128, 64, 64, 64),
    "MOUNTAIN": pygame.Rect(192, 64, 64, 64),
}
house_rects = {
    "HOUSE1": pygame.Rect(0, 0, 16, 16),
    "HOUSE2": pygame.Rect(16, 0, 16, 16),
    "HOUSE3": pygame.Rect(32, 0, 16, 16),
    "HOUSE4": pygame.Rect(48, 0, 16, 16),
    "MILL"  : pygame.Rect(0, 16, 16, 16),
    "LUMBER": pygame.Rect(16, 16, 16, 16),
    "CAVE"  : pygame.Rect(32, 16, 16, 16),
    "FARM"  : pygame.Rect(48, 16, 16, 16),
    "FARMLAND" : pygame.Rect(48, 32, 16, 16),
    "MARKET" : pygame.Rect(32, 32, 16, 16),
    "FOREST" : pygame.Rect(48, 64, 16, 16),
    "HOUSE5": pygame.Rect(0, 48, 16, 16),
    "WATERWHEEL" : pygame.Rect(48, 48, 16, 16),
}

tiles = {name: full_tilemap.subsurface(rect) for name, rect in tile_rects.items()}

houses = {name: house_tilemap.subsurface(rect) for name, rect in house_rects.items()}
