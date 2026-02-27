import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill("purple")          # 这里指定颜色
pygame.display.flip()          # 或者 pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()