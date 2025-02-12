import buildings as n
from config.const import *
import menu

pygame.init()

clock = pygame.time.Clock()
allsprites = pygame.sprite.Group()
btns = pygame.sprite.Group()
clock.tick(60)
m = n.ClickMap(sc, "saves/firstmap.txt")
tf[0] = True
mu = menu.menu.menu()
#allsprites.add()


while run:
    sc.fill((88, 88, 88))
    for event in pygame.event.get():
        if tf[0]:
            mu.use(event)
        if event.type == pygame.QUIT:
            run = False

    allsprites.update()


    if tf[0]:
        mu.draw()

    if tf[1]:
        m.draw(sc)
        m.update()
        


    allsprites.draw(sc)
    pygame.display.flip()

safe_exit = True
text = font.render("Are you sure to exit?", True, (255, 255, 255))
mark = safe()
while safe_exit:
    sc.fill((88, 88, 88))
    sc.blit(text, (1152/3, 320))



    pygame.display.flip()


pygame.quit()