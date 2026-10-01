import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da Janela
LARGURA = 1000
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Futebol Arcade em Python")

# Cores (RGB)
GRAMADO = (34, 139, 34)
LINHA = (255, 255, 255)
TRAVE = (240, 240, 240)
COR_P1 = (30, 144, 255)   # Azul
COR_P2 = (220, 20, 60)    # Vermelho
COR_BOLA = (255, 255, 255)
COR_TEXTO = (255, 255, 255)

# Relógio para controlar o FPS
relogio = pygame.time.Clock()
FPS = 60

# Configurações do Campo e Traves
ALTURA_TRAVE = 150
Y_TRAVE_CIMA = (ALTURA // 2) - (ALTURA_TRAVE // 2)
Y_TRAVE_BAIXO = Y_TRAVE_CIMA + ALTURA_TRAVE

# Parâmetros dos Jogadores
RAIO_JOGADOR = 25
VEL_JOGADOR = 5

# Parâmetros da Bola
RAIO_BOLA = 12
atrito_bola = 0.98

# Placar
pontos_p1 = 0
pontos_p2 = 0
fonte = pygame.font.SysFont("Arial", 40, bold=True)

class Jogador:
    def __init__(self, x, y, cor, p_id):
        self.x = x
        self.y = y
        self.cor = cor
        self.p_id = p_id

    def mover(self, teclas):
        # Controles do Jogador 1 (WASD)
        if self.p_id == 1:
            if teclas[pygame.K_w] and self.y - RAIO_JOGADOR > 0:
                self.y -= VEL_JOGADOR
            if teclas[pygame.K_s] and self.y + RAIO_JOGADOR < ALTURA:
                self.y += VEL_JOGADOR
            if teclas[pygame.K_a] and self.x - RAIO_JOGADOR > 0:
                self.x -= VEL_JOGADOR
            if teclas[pygame.K_d] and self.x + RAIO_JOGADOR < LARGURA:
                self.x += VEL_JOGADOR
        
        # Controles do Jogador 2 (Setas)
        elif self.p_id == 2:
            if teclas[pygame.K_UP] and self.y - RAIO_JOGADOR > 0:
                self.y -= VEL_JOGADOR
            if teclas[pygame.K_DOWN] and self.y + RAIO_JOGADOR < ALTURA:
                self.y += VEL_JOGADOR
            if teclas[pygame.K_LEFT] and self.x - RAIO_JOGADOR > 0:
                self.x -= VEL_JOGADOR
            if teclas[pygame.K_RIGHT] and self.x + RAIO_JOGADOR < LARGURA:
                self.x += VEL_JOGADOR

    def desenhar(self):
        pygame.draw.circle(tela, self.cor, (int(self.x), int(self.y)), RAIO_JOGADOR)
        pygame.draw.circle(tela, (0, 0, 0), (int(self.x), int(self.y)), RAIO_JOGADOR, 2)

class Bola:
    def __init__(self):
        self.resetar()

    def resetar(self):
        self.x = LARGURA // 2
        self.y = ALTURA // 2
        self.dx = 0
        self.dy = 0

    def mover(self):
        self.x += self.dx
        self.y += self.dy
        
        # Aplicar atrito para a bola parar gradualmente
        self.dx *= atrito_bola
        self.dy *= atrito_bola

        # Colisão com as paredes laterais (fora das traves)
        if self.y < Y_TRAVE_CIMA or self.y > Y_TRAVE_BAIXO:
            if self.x - RAIO_BOLA < 0:
                self.x = RAIO_BOLA
                self.dx *= -1
            elif self.x + RAIO_BOLA > LARGURA:
                self.x = LARGURA - RAIO_BOLA
                self.dx *= -1

        # Colisão com o teto e chão
        if self.y - RAIO_BOLA < 0:
            self.y = RAIO_BOLA
            self.dy *= -1
        elif self.y + RAIO_BOLA > ALTURA:
            self.y = ALTURA - RAIO_BOLA
            self.dy *= -1

    def colidir_jogador(self, jogador):
        dist_x = self.x - jogador.x
        dist_y = self.y - jogador.y
        distancia = (dist_x**2 + dist_y**2)**0.5
        dist_minima = RAIO_JOGADOR + RAIO_BOLA

        if distancia < dist_minima:
            if distancia == 0: distancia = 1
            nx = dist_x / distancia
            ny = dist_y / distancia

            self.x = jogador.x + nx * dist_minima
            self.y = jogador.y + ny * dist_minima

            # Chute / Impulso ao encostar na bola
            self.dx = nx * 8
            self.dy = ny * 8

    def desenhar(self):
        pygame.draw.circle(tela, COR_BOLA, (int(self.x), int(self.y)), RAIO_BOLA)
        pygame.draw.circle(tela, (0, 0, 0), (int(self.x), int(self.y)), RAIO_BOLA, 1)

# Inicialização dos objetos
p1 = Jogador(200, ALTURA // 2, COR_P1, 1)
p2 = Jogador(800, ALTURA // 2, COR_P2, 2)
bola = Bola()

def reiniciar_posicoes():
    p1.x, p1.y = 200, ALTURA // 2
    p2.x, p2.y = 800, ALTURA // 2
    bola.resetar()

# Loop Principal do Jogo
while True:
    # CORREÇÃO AQUI: Captura os eventos corretamente do Pygame
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Captura de teclas pressionadas
    teclas = pygame.key.get_pressed()
    
    # Atualizações de Movimento e Colisões
    p1.mover(teclas)
    p2.mover(teclas)
    bola.mover()
    
    bola.colidir_jogador(p1)
    bola.colidir_jogador(p2)

    # Verificação de Gol
    if bola.x < 0:
        pontos_p2 += 1
        reiniciar_posicoes()
    elif bola.x > LARGURA:
        pontos_p1 += 1
        reiniciar_posicoes()

    # --- Desenhar na Tela ---
    tela.fill(GRAMADO)
    
    # Linhas do campo
    pygame.draw.line(tela, LINHA, (LARGURA // 2, 0), (LARGURA // 2, ALTURA), 3)
    pygame.draw.circle(tela, LINHA, (LARGURA // 2, ALTURA // 2), 100, 3)
    
    # Desenhar as Traves
    pygame.draw.rect(tela, TRAVE, (0, Y_TRAVE_CIMA, 10, ALTURA_TRAVE))
    pygame.draw.rect(tela, TRAVE, (LARGURA - 10, Y_TRAVE_CIMA, 10, ALTURA_TRAVE))

    # Desenhar Entidades
    p1.desenhar()
    p2.desenhar()
    bola.desenhar()

    # Desenhar Placar
    texto_placar = fonte.render(f"{pontos_p1}   x   {pontos_p2}", True, COR_TEXTO)
    tela.blit(texto_placar, (LARGURA // 2 - texto_placar.get_width() // 2, 20))

    # Atualiza a tela
    pygame.display.flip()
    relogio.tick(FPS)