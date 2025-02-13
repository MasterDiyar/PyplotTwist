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

loadnew = menu.menu.choosemenu()
b = menu.menu.exitmenu()
mu = menu.menu.menu()
#allsprites.add()


while run:
    sc.fill((88, 88, 88))
    for event in pygame.event.get():
        if tf[0]:
            mu.use(event)
        if tf[1]:
            loadnew.use(event)
        if event.type == pygame.QUIT:
            run = False

    allsprites.update()


    if tf[0]:
        mu.draw()
    if tf[1]:
        loadnew.draw()

    if tf[2]:
        m.draw(sc)
        m.update()
        


    allsprites.draw(sc)
    pygame.display.flip()

safe_exit = True
safer= False
text = font.render("Are you want to save?", True, (255, 255, 255))


while safe_exit:
    sc.fill((88, 88, 88))
    sc.blit(text, (1152/3, 320))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            safe_exit = False
        tfler = b.use(event)
        if tfler[0]:
            safer = True
            safe_exit = False
        if tfler[1]:
            safe_exit = False

    b.draw()

    pygame.display.flip()
if safer:
    print(m.nmap)
    text = ""
    for columm in m.nmap:
        for row in columm:
            text += text+ " " +str(row)
        text += "\n"

    with open("saves/firstmap.info", "w") as f:
        f.write(text)

pygame.quit()