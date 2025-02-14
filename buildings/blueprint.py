from config.const import *
from config.Decoder import decoder

class Blueprint:
    def __init__(self):
        self.chertezhdown = pygame.image.load("buildings/image/chertezh.png").convert_alpha()
        self.surface = pygame.Surface(self.chertezhdown.get_size(), pygame.SRCALPHA)
        self.chertezhup = pygame.image.load("buildings/image/chertezh_verk.png").convert_alpha()
        self.chertezh = []
        self.chertezh.append(self.chertezhdown)
        self.chertezh.append(pygame.image.load("buildings/image/waterwheel.png").convert_alpha())
        self.chertezh.append(self.chertezhup)
    def draw(self, screen):
        for detail in self.chertezh:
            self.surface.blit(detail, detail.get_rect())
        screen.blit(self.surface, map_margin)
        print(self.chertezh)
    def add(self, detail):
        self.chertezh.insert(-1, detail)
    def clear(self):
        self.chertezh = [self.chertezhdown, self.chertezhup]

class Building(Blueprint):
    def __init__(self):
        Blueprint.__init__(self)
        self.nmap = []

    def reader(self, pos:tuple):
        with open("saves/firstmap.info", "r") as f:
            m = f.readlines()
        self.nmap= []
        for line in m:
            c = line.split(" ")[:-1]
            c.append((line.split(" ")[-1])[0:2])
            self.nmap.append(c)
        l =  decoder(self.nmap, "farm", pos).split("#")
        for i in l:

            self.add(self.mader(i))

    def mader(self, a):
        n = pygame.image.load("buildings/image/"+a+".png").convert_alpha()
        return n

