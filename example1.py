import pygame

pygame.init()

screenw = 800
screenh = 600

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0 , 255)

gameDisplay = pygame.display.set_mode([screenw, screenh])
pygame.display.set_caption('Slither')
# same as pygame.display.flip()
pygame.display.update()

gameExit = False
while not gameExit:
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    # general game logic
    gameDisplay.fill(green)
    pygame.draw.rect(gameDisplay, black, [50, 50, 100, 100])
    pygame.draw.rect(gameDisplay, red, [50, 50, 100, 10])

    pygame.display.update()

pygame.quit()
quit()
