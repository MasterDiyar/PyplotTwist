from config.const import *

class Blueprint:
    def __init__(self):
        self.chertezh = pygame.image.load("chertezh.png")
        self.surface = pygame.Surface(self.chertezh.get_size())
        self.chertezhdown = pygame.image.load("chertezh_verk.png")
    def draw(self, screen):
        self.surface.blits([(self.chertezh, (0,0)), self.chertezhdown, (0,0)])
        screen.blit(self.surface, map_margin)