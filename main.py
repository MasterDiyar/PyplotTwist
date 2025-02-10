import buildings as n
from config.const import *
import menu

pygame.init()

clock = pygame.time.Clock()
allsprites = pygame.sprite.Group()
clock.tick(60)
m = n.ClickMap(sc, "saves/firstmap.txt")
l = m.draw()
tf[0] = True
mu = menu.menu.menu()
#allsprites.add()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    sc.fill((88, 88, 88))
    allsprites.update()
    if tf[0]:
        mu.use()


    if tf[1]:
        sc.blit(l, map_margin)    
        m.update()
        


    allsprites.draw(sc)
    pygame.display.flip()


pygame.quit()