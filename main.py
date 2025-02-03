import pygame
from player.player import Player
pygame.init()
sc = pygame.display.set_mode((1000, 800))

run = True
clock = pygame.time.Clock()
allsprites = pygame.sprite.Group()

player = Player(sc, "player/images/Idle.png", group=allsprites)

allsprites.add(player)
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    sc.fill((188, 188, 188))
    allsprites.update()




    allsprites.draw(sc)
    pygame.display.flip()


pygame.quit()