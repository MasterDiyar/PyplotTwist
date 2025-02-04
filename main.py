import pygame
import buildings.connected as n
from config.const import *

pygame.init()

run = True
clock = pygame.time.Clock()
allsprites = pygame.sprite.Group()
clock.tick(60)
m = n.Map(sc, "saves/firstmap.txt")
l = m.draw()


#allsprites.add()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    sc.fill((88, 88, 88))
    allsprites.update()

    sc.blit(l,(128,64))    



    allsprites.draw(sc)
    pygame.display.flip()


pygame.quit()