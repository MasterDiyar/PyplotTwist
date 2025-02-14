from .const import *
from .Button import *

def drawtext(screen, text, pos, color):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, pos)