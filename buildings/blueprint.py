from config.const import *

class Blueprint:
    def __init__(self):
        self.chertezh = pygame.image.load("buildings/image/chertezh.png").convert_alpha()
        self.surface = pygame.Surface(self.chertezh.get_size())
        self.chertezhdown = pygame.image.load("buildings/image/chertezh_verk.png").convert_alpha()
    def draw(self, screen):
        self.surface.blit(self.chertezh, self.chertezh.get_rect())
        self.surface.blit(self.chertezhdown, self.chertezhdown.get_rect())
        screen.blit(self.surface, map_margin)