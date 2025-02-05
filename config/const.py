import pygame

sc = pygame.display.set_mode((1152, 768))
run = True

map_margin = (128, 64)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (88, 88, 88)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

full_tilemap = pygame.image.load("buildings/image/tilemap.png").convert_alpha()

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

tiles = {name: full_tilemap.subsurface(rect) for name, rect in tile_rects.items()}
    