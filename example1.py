import pygame


pygame.init()

screenw = 800
screenh = 800

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

#variables for snake
lead_x = 300
lead_y = 300
lead_x_change = 0
lead_y_change = 0

clock = pygame.time.Clock()

while not gameExit:
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -10
                lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = 10
                lead_y_change = 0
            elif event.key == pygame.K_UP:
                lead_y_change = -10
                lead_x_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = 10
                lead_x_change = 0

    # snake logic
    if lead_x > screenw or lead_x < 0 or lead_y > screenh or lead_y < 0:
        gameExit = True

    lead_x += lead_x_change
    lead_y += lead_y_change

    # color logic
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, screenw / 100, screenh / 100])
    pygame.display.update()

    clock.tick(120)

pygame.quit()
quit()
