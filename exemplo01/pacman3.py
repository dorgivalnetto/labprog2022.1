import pygame

pygame.init()

tela = pygame.display.set_mode((800, 600), 0)
AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)


class Pacman:
    def __init__(self):
        # definindo as coordenadas do ponto central do círculo
        self.centro_x = 400
        self.centro_y = 300
        self.tamanho = 100
        # vamos pegar apenas a parte inteira da divisão com //
        self.raio = self.tamanho // 2

        #definindo a velocidade de movimentação
        self.velocidade_x = 1
        self.velocidade_y = 1

    #verifica a colisão do Pacman com a tela
    def calcular_regras(self):
        self.centro_x += self.velocidade_x
        self.centro_y += self.velocidade_y

        if self.centro_x + self.raio > 800:
            self.velocidade_x = -1
        if self.centro_x - self.raio < 0:
            self.velocidade_x = 1
        if self.centro_y + self.raio > 600:
            self.velocidade_y = -1
        if self.centro_y - self.raio < 0:
            self.velocidade_y = 1

    # criando o método pintar
    def pintar(self, tela):
        # desenhando o Pacman
        pygame.draw.circle(tela, AMARELO, (self.centro_x, self.centro_y), self.raio, 0)

        # desenhando a boca do Pacman
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
        labio_inferior = (self.centro_x + self.raio, self.centro_y)
        pontos = [canto_boca, labio_superior, labio_inferior]

        pygame.draw.polygon(tela, PRETO, pontos, 0)

        # desenhando o olho do Pacman
        olho_x = int(self.centro_x + self.raio / 5)
        olho_y = int(self.centro_y - self.raio * 0.6)
        olho_raio = int(self.raio / 10)

        pygame.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio, 0)


if __name__ == "__main__":
    pacman = Pacman()

    # loop do jogo
    while True:
        # calcular as regras
        pacman.calcular_regras()

        # pintar na tela
        tela.fill(PRETO)
        pacman.pintar(tela)
        pygame.display.update()

        # captura os eventos
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
