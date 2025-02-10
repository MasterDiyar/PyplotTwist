import pygame
import pygame.sprite

from config import BLACK


class Button:
    def __init__(self, colour, screen,x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.screen =screen
        self.colour = colour
        self.clicked = False
    def update(self):
        self.clicked = False
        pygame.draw.rect(self.screen, self.colour, self.rect)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(f"Clicked in{pygame.mouse.get_pos()}")
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    self.clicked = True
        return self.clicked
    def getpos(self):
        return self.rect.topleft

class ImageButton(Button, pygame.sprite.Sprite):
    def __init__(self, screen, image):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.screen = screen
        a = self.rect
        super().__init__(Button(self, BLACK, screen, a.x, a.y, a.width, a.height), pygame.sprite.Sprite(self) )
    def update(self):
        self.clicked = False
        self.screen.blit(self.image, self.rect)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    self.clicked = True
        return self.clicked






        