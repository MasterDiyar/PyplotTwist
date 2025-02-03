import pygame

class Carcase(pygame.sprite.Sprite):
    def __init__(self, image="images/default.png", position=(0,0), hitbox=None, heal_point = 1):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.rotozoom(pygame.image.load(image), 0, 1)
        self.position = position
        self.heal_point = heal_point
        if hitbox is not None:self.rect = hitbox
        else:self.rect = self.image.get_rect()
        self.rect.center = position



