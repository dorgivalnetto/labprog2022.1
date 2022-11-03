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
        #vamos definir a quantidade de células que existirá na tela
        self.tamanho = 800 // 30
        # vamos pegar apenas a parte inteira da divisão com //
        self.raio = self.tamanho // 2

        #definindo a velocidade de movimentação
        self.velocidade_x = 0
        self.velocidade_y = 0

        #definindo a movimentação em linhas e colunas
        self.coluna = 1
        self.linha = 1

    #verifica a colisão do Pacman com a tela
    def calcular_regras(self):
        self.coluna += self.velocidade_x
        self.linha += self.velocidade_y

        #coluna_atual * tamanho
        self.centro_x = int(self.coluna * self.tamanho + self.raio)
        self.centro_y = int(self.linha * self.tamanho + self.raio)



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


    def processar_eventos(self, eventos):
        for e in eventos:
            if e.type == pygame.KEYDOWN:
                # seta para a direita pressionada
                if e.key == pygame.K_RIGHT:
                    self.velocidade_x = 1
                elif e.key == pygame.K_LEFT:
                    self.velocidade_x = -1
                elif e.key == pygame.K_UP:
                    self.velocidade_y = -1
                elif e.key == pygame.K_DOWN:
                    self.velocidade_y = 1

            # seta solta
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT:
                    self.velocidade_x = 0
                elif e.key == pygame.K_LEFT:
                    self.velocidade_x = 0
                elif e.key == pygame.K_UP:
                    self.velocidade_y = 0
                elif e.key == pygame.K_DOWN:
                    self.velocidade_y = 0

    def processar_eventos_mouse(self, eventos):
        delay = 100
        for e in eventos:
            if e.type == pygame.MOUSEMOTION:
                #pos contém o x e o y
                mouse_x, mouse_y = e.pos
                self.coluna = (mouse_x - self.centro_x) / delay
                self.linha = (mouse_y - self.centro_y) / delay

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
        pygame.time.delay(150)

        # captura os eventos
        eventos = pygame.event.get()
        for e in eventos:
            if e.type == pygame.QUIT:
                exit()
            pacman.processar_eventos(eventos)
            #pacman.processar_eventos_mouse(eventos)
