import pygame

AMARELO = (255, 255, 0)
PRETO = (0,0,0)
RAIO = 50

pygame.init()

tela = pygame.display.set_mode((640, 480), 0)
x = 10
velocidade_x = 0.1

y = 10
velocidade_y = 0.5

#loop do jogo =
while True:

    #Calcula as regras
    x += velocidade_x
    y += velocidade_y

    if x + RAIO > 640:
        velocidade_x = -0.1
    if x - RAIO < 0:
        velocidade_x = 0.1
    if y + RAIO > 480:
        velocidade_y = -0.5
    if y - RAIO < 0:
        velocidade_y = 0.5

    #Desenha na tela
    #antes de desenhar na tela, vamos pintá-la de preto
    tela.fill(PRETO)

    pygame.draw.circle(tela, AMARELO, (int(x), int(y)), RAIO, 0)

    #atualizar a tela mostrando o círculo
    pygame.display.update()


    #Eventos do usuário

    #Verificar se a tela foi fechada
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()