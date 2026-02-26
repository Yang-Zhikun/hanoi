import pygame
pygame.init()
screen = pygame.display.set_mode(800, 600)
running = True
while running:
    for event in screen.event.get():
        if event == pygame.QUIT:
            running = False

pygame.quit()