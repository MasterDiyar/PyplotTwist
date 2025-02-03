import pygame

class Carcase(pygame.sprite.Sprite):
    def __init__(self, image:str="images/default.png", position:tuple=(0,0), hitbox=None, heal_point = 1, rotation = 0, scale = 1):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.rotozoom(pygame.image.load(image), rotation, scale)
        self.position = position
        self.heal_point = heal_point
        if hitbox is not None:self.rect = hitbox
        else:self.rect = self.image.get_rect()
        self.rect.center = position

def rect_addiction(rect1:pygame.Rect, objected):
    if objected is tuple:
        rect = pygame.Rect(rect1.x + objected[0], rect1.y + objected[1], rect1.width, rect1.height)
        return rect
    elif objected is pygame.Rect:
        rect = pygame.Rect(rect1.x + objected.x, rect1.y + objected.y, rect1.width, rect1.height)
        return rect
    else:
        rect = rect1
        print("Not rect or tuple exception")
        return rect