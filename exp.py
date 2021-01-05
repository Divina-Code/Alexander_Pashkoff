import pygame
radious = 15
pygame.init()
gamedisplay = pygame.display.set_mode((800, 600))
gamedisplay.fill((255, 255, 255))
game = True
while game:
    event = pygame.event.get()
    for e in event:
        if e.type == pygame.QUIT:
            game = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 4:
                radious += 1
            if e.button == 5:
                radious -= 1
    if pygame.mouse.get_pressed()[0]:
        mousepose = pygame.mouse.get_pos()
        pygame.draw.circle(gamedisplay, (255, 0, 0), mousepose, radious)
    pygame.display.update()
pygame.quit()
