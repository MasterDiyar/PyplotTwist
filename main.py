import pygame

pygame.init()
sc = pygame.display.set_mode((1000, 800))

run = True
clock = pygame.time.Clock()
allsprites = pygame.sprite.Group()
clock.tick(60)


#allsprites.add()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    sc.fill((88, 88, 88))
    allsprites.update()





    allsprites.draw(sc)
    pygame.display.flip()


pygame.quit()