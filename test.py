import pygame

from Techtree import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

n = 200

tree = TechTree()
tree.add_tech("Mining", 100, 100)
tree.add_tech("Advanced Mining", 300, 120, ["Mining"], {"stone":500})
tree.add_tech("Metalnotworking", 100, 200, ["Mining"])
tree.add_tech("Metalworking", 500, 300, ["Metalnotworking","Advanced Mining"])




tree.save_file("saves/tech_tree.txt")

running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            tree.handle_click(event.pos)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:

                n = 500

    tree.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()


