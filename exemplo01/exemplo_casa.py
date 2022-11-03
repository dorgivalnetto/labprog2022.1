import pygame
pygame.init()
tela = pygame.display.set_mode((640, 480), 0)

while True:
    pygame.draw.rect(tela, (255, 0, 0), (212, 100, 200, 200), 5)
    r = pygame.Rect(376, 231, 200, 200)
    pygame.draw.rect(tela, (255, 167, 0), r, 5)
    pygame.draw.polygon(tela, (255, 0, 0), [(100, 100), (200, 200), (100, 200)], 5)


    pygame.draw.line(tela, (255, 255, 0), (320, 0), (600, 240), 5)
    pygame.draw.line(tela, (255, 255, 0), (320, 0), (40, 240), 5)
    pygame.draw.rect(tela, (255, 255, 0), ((40, 240), (560, 200)), 5)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
