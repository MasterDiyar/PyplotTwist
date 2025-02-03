from .carcase import *
import math
class Bullet(Carcase):
    def __init__(self, x, y, speed, rotation):
        Carcase.__init__(self, 'player/images/WallHang.png',position=(x, y), rotation=rotation)
        self.time = pygame.time.get_ticks()
        self.speed = speed
        self.rotation = rotation
    def update(self):
        self.rect.x += math.cos(self.rotation) * self.speed
        self.rect.y += math.sin(self.rotation) * self.speed
        self.timer = pygame.time.get_ticks()
        if self.timer > self.time + 3000:
            self.kill()

