import pygame
import pygame.sprite

from config import *
from config.const import *

class Button:
    def __init__(self, colour, screen,x, y, width, height, name = "none"):
        self.name = name
        self.rect = pygame.Rect(x, y, width, height)
        self.screen =screen
        self.colour = colour
        self.clicked = False
    def update(self, event):
        self.clicked = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.clicked = True

        return self.clicked
    def draw(self):
        self.clicked = False
        pygame.draw.rect(self.screen, self.colour, self.rect, border_radius=5)
    def getpos(self):
        return self.rect.topleft

class ImageButton(Button, pygame.sprite.Sprite):
    def __init__(self, screen, image, name = "none"):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.screen = screen
        a = self.rect
        super().__init__(Button(self, BLACK, screen, a.x, a.y, a.width, a.height, name), pygame.sprite.Sprite(self) )
    def update(self, event):
        self.clicked = False
        self.screen.blit(self.image, self.rect)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.clicked = True
        return self.clicked

class TextButton(Button):
    def __init__(self, screen, pos, text, color, name="none"):
        self.pos = pos
        self.width = 9 * len(text) + 30
        self.text = font.render(text, True, BLACK)
        self.screen = screen
        self.name = name if name!="none" else text
        super().__init__(color, self.screen, pos[0], pos[1], self.width, 50)
    def draw(self):
        pygame.draw.rect(self.screen, self.colour, self.rect, border_radius=15)
        self.screen.blit(self.text, (self.rect.x+15, self.rect.y+15))
        self.clicked = False

class ButtonBox:
    def __init__(self):
        self.buttons = []

    def add(self, button):
        self.buttons.append(button)
    def draw(self):
        for button in self.buttons:
            button.draw()
    def update(self, event):
        for button in self.buttons:
            button.update(event)
    def getname(self, name, event):
        for button in self.buttons:
            if button.name == name:
                return button.update(event)

class GoldenButton(Button):
    def __init__(self, screen, pos, text, color):
        self.pos = pos
        self.width = 9 * len(text) + 30
        self.text = font.render(text, True, BLACK)
        self.screen = screen
        self.clicked = False
        self.goldenrect = pygame.Rect(self.pos[0]-5, self.pos[1]-5, self.width+10, 60)
        super().__init__(color, self.screen, pos[0], pos[1], self.width, 50)
    def draw(self):
        pygame.draw.rect(self.screen, GOLDEN, self.goldenrect, border_radius=20)
        pygame.draw.rect(self.screen, self.colour, self.rect, border_radius=15)
        self.screen.blit(self.text, (self.rect.center[0]-self.width/4, self.rect.y+15))
        self.clicked = False


        