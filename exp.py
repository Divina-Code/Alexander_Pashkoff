import pygame,random
radious = 15
pygame.init()
gamedisplay = pygame.display.set_mode((800, 600))
gamedisplay.fill((255, 255, 255))
acolor = 0
scolor = 0
dcolor = 0
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
            if e.button == pygame.BUTTON_RIGHT:
                acolor = random.randint(0, 255)
                scolor = random.randint(0, 255)
                dcolor = random.randint(0, 255)
    if pygame.mouse.get_pressed()[0]:
        mousepose = pygame.mouse.get_pos()
        pygame.draw.circle(gamedisplay, (acolor, scolor, dcolor), mousepose, radious)
    pygame.display.update()
pygame.quit()
