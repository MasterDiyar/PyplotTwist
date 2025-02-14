import buildings as n
from buildings import Building
from config import *
import menu
import game
pygame.init()

clock = pygame.time.Clock()
clock.tick(60)
tf[0] = True
the_game = game.Game("EASY")
b = menu.menu.exitmenu()
mu = menu.menu.menu()

while run:
    sc.fill((88, 88, 88))
    for event in pygame.event.get():
        if tf[0]:
            randomval = mu.use(event)
            if randomval is not None:
                the_game = game.Game(randomval)

        if tf[2]:
            the_game.update(event)
        if event.type == pygame.QUIT:
            run = False



    if tf[0]:
        mu.draw()


    if tf[2]:
        the_game.draw()

    if tf[3]:
        with open("saves/final.txt", "r") as f:
            drawtext(sc, f.readline(), (128, 128), (255, 255, 255))
        

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
m = Building()
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