import pygame

import DisplayEngine

displayEngine = DisplayEngine.DisplayEngine()
displayEngine.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            displayEngine.quit()
            exit()