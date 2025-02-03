import pygame

class Button:
    def __init__(self, colour, screen,x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.screen =screen
        self.colour = colour
    def clicked(self):
        return True
    def update(self, event):
        pygame.draw.rect(self.screen, self.colour, self.rect)
        if event == pygame.MOUSEBUTTONDOWN and :
            return self.clicked()
        