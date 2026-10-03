# pygame: biblioteca usada para criar a janela, desenhar o campo e controlar o jogo.
# sys: permite encerrar o programa corretamente.
import pygame
import sys

# Inicializa o Pygame antes de usar seus recursos.
pygame.init()

# Define o tamanho da janela do jogo em pixels.
# X = largura e Y = altura.
LARGURA = 1000
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Futebol Arcade em Python - PYGAME")

# Cores no formato RGB: (Vermelho, Verde, Azul).
# Cada valor vai de 0 a 255.
GRAMADO = (34, 139, 34)
LINHA = (255, 255, 255)
TRAVE = (240, 240, 240)
COR_P1 = (30, 144, 255)   # Azul
COR_P2 = (220, 20, 60)    # Vermelho
COR_BOLA = (255, 255, 255)
COR_TEXTO = (255, 255, 255)

# Clock controla quantas vezes o jogo atualiza por segundo.
# FPS = 60 significa aproximadamente 60 atualizações por segundo.
# TEMPO_PARTIDA = 120 segundos = 2 minutos.
# inicio_partida guarda o momento em que a partida começou.
relogio = pygame.time.Clock()
FPS = 60
TEMPO_PARTIDA = 120
inicio_partida = pygame.time.get_ticks()

# Define o tamanho e a posição vertical da abertura das traves.
# Como a janela tem 600 pixels de altura, a abertura vai de Y=225 até Y=375.
ALTURA_TRAVE = 150
Y_TRAVE_CIMA = 225
Y_TRAVE_BAIXO = 375

# Define o tamanho e a velocidade dos jogadores.
RAIO_JOGADOR = 25
VEL_JOGADOR = 5

# Define o tamanho da bola e o atrito.
# Quanto mais próximo de 1, mais tempo a bola continua se movimentando.
RAIO_BOLA = 15
atrito_bola = 0.98

# Variáveis que armazenam os gols de cada jogador.
pontos_p1 = 0
pontos_p2 = 0
fonte = pygame.font.SysFont("Arial", 40, bold=True)

# Classe que representa um jogador.
# Uma classe é um modelo que reúne dados e comportamentos de um objeto.
class Jogador:
    # Cria um jogador recebendo posição, cor e identificação.
    def __init__(self, x, y, cor, p_id):
        # Posição horizontal do jogador.
        self.x = x
        # Posição vertical do jogador.
        self.y = y
        # Cor usada para desenhar o jogador.
        self.cor = cor
        # Identifica se é o jogador 1 ou 2.
        self.p_id = p_id
        # Primeiro zeramos o movimento. Depois ele recebe valor se alguma tecla for pressionada.
        self.dx = 0
        self.dy = 0

    # Lê as teclas pressionadas e movimenta o jogador.
    def mover(self, teclas):
        self.dx = 0
        self.dy = 0

        # Jogador 1 usa W, A, S e D.
        if self.p_id == 1:
            if teclas[pygame.K_w] and self.y - RAIO_JOGADOR > 0:
                self.y -= VEL_JOGADOR
                self.dy = -VEL_JOGADOR
            if teclas[pygame.K_s] and self.y + RAIO_JOGADOR < ALTURA:
                self.y += VEL_JOGADOR
                self.dy = VEL_JOGADOR
            if teclas[pygame.K_a] and self.x - RAIO_JOGADOR > 0:
                self.x -= VEL_JOGADOR
                self.dx = -VEL_JOGADOR
            if teclas[pygame.K_d] and self.x + RAIO_JOGADOR < LARGURA:
                self.x += VEL_JOGADOR
                self.dx = VEL_JOGADOR
        
        # Jogador 2 usa as setas do teclado.
        elif self.p_id == 2:
            if teclas[pygame.K_UP] and self.y - RAIO_JOGADOR > 0:
                self.y -= VEL_JOGADOR
                self.dy = -VEL_JOGADOR
            if teclas[pygame.K_DOWN] and self.y + RAIO_JOGADOR < ALTURA:
                self.y += VEL_JOGADOR
                self.dy = VEL_JOGADOR
            if teclas[pygame.K_LEFT] and self.x - RAIO_JOGADOR > 0:
                self.x -= VEL_JOGADOR
                self.dx = -VEL_JOGADOR
            if teclas[pygame.K_RIGHT] and self.x + RAIO_JOGADOR < LARGURA:
                self.x += VEL_JOGADOR
                self.dx = VEL_JOGADOR

    # Desenha a bola como um círculo.
    def desenhar(self):
        pygame.draw.circle(tela, self.cor, (int(self.x), int(self.y)), RAIO_JOGADOR)
        pygame.draw.circle(tela, (0, 0, 0), (int(self.x), int(self.y)), RAIO_JOGADOR, 2)

# Classe que representa a bola.
class Bola:
    def __init__(self):
        self.resetar()

    # Coloca a bola novamente no centro e zera sua velocidade.
    def resetar(self):
        self.x = LARGURA // 2
        self.y = ALTURA // 2
        self.dx = 0
        self.dy = 0

    # Atualiza a posição da bola usando sua velocidade.
    def mover(self):
        self.x += self.dx
        self.y += self.dy
        
        # O atrito reduz a velocidade aos poucos até a bola parar.
        self.dx *= atrito_bola
        self.dy *= atrito_bola

        # Fora da abertura do gol, as laterais funcionam como paredes.
        if self.y < Y_TRAVE_CIMA or self.y > Y_TRAVE_BAIXO:
            if self.x - RAIO_BOLA < 0:
                self.x = RAIO_BOLA
                self.dx *= -1
            elif self.x + RAIO_BOLA > LARGURA:
                self.x = LARGURA - RAIO_BOLA
                self.dx *= -1

        # Impede a bola de sair pelo teto ou pelo chão.
        if self.y - RAIO_BOLA < 0:
            self.y = RAIO_BOLA
            self.dy *= -1
        elif self.y + RAIO_BOLA > ALTURA:
            self.y = ALTURA - RAIO_BOLA
            self.dy *= -1

    # Verifica se a bola encostou no jogador.
    # Se encostar, a bola é afastada e recebe o impulso do movimento do jogador.
    def colidir_jogador(self, jogador):
        dist_x = self.x - jogador.x
        dist_y = self.y - jogador.y
        # Calcula a distância entre o centro da bola e o centro do jogador.
        distancia = (dist_x**2 + dist_y**2)**0.5
        # A soma dos raios define quando os dois círculos estão encostando.
        dist_minima = RAIO_JOGADOR + RAIO_BOLA

        if distancia < dist_minima:
            if distancia == 0: distancia = 1
            # nx e ny indicam a direção da colisão.
            nx = dist_x / distancia
            ny = dist_y / distancia

            self.x = jogador.x + nx * dist_minima
            self.y = jogador.y + ny * dist_minima

            # A bola recebe o impulso na mesma direção em que o jogador está andando.
        # Isso faz o comportamento ser igual para os dois jogadores.
            if jogador.dx != 0 or jogador.dy != 0:
                self.dx = jogador.dx * 1.6
                self.dy = jogador.dy * 1.6

    def desenhar(self):
        pygame.draw.circle(tela, COR_BOLA, (int(self.x), int(self.y)), RAIO_BOLA)
        pygame.draw.circle(tela, (0, 0, 0), (int(self.x), int(self.y)), RAIO_BOLA, 1)

# Impede que os dois jogadores ocupem o mesmo espaço.
# A função calcula a distância entre eles e os separa quando encostam.
def impedir_colisao_jogadores():
    dist_x = p1.x - p2.x
    dist_y = p1.y - p2.y
    distancia = (dist_x**2 + dist_y**2)**0.5
    distancia_minima = RAIO_JOGADOR * 2

    if distancia < distancia_minima:
        if distancia == 0:
            distancia = 1

        nx = dist_x / distancia
        ny = dist_y / distancia
        ajuste = (distancia_minima - distancia) / 2

        p1.x += nx * ajuste
        p1.y += ny * ajuste
        p2.x -= nx * ajuste
        p2.y -= ny * ajuste

        p1.x = max(RAIO_JOGADOR, min(LARGURA - RAIO_JOGADOR, p1.x))
        p1.y = max(RAIO_JOGADOR, min(ALTURA - RAIO_JOGADOR, p1.y))
        p2.x = max(RAIO_JOGADOR, min(LARGURA - RAIO_JOGADOR, p2.x))
        p2.y = max(RAIO_JOGADOR, min(ALTURA - RAIO_JOGADOR, p2.y))


# Cria os dois jogadores e a bola.
p1 = Jogador(200, ALTURA // 2, COR_P1, 1)
p2 = Jogador(800, ALTURA // 2, COR_P2, 2)
bola = Bola()

# Volta jogadores e bola para as posições iniciais.
def reiniciar_posicoes():
    p1.x, p1.y = 200, ALTURA // 2
    p2.x, p2.y = 800, ALTURA // 2
    bola.resetar()

# Loop principal: fica executando enquanto o jogo estiver aberto.
# Cada repetição atualiza eventos, movimentos, colisões e desenho da tela.
while True:
    # Calcula quantos segundos ainda faltam para terminar a partida.
    tempo_restante = TEMPO_PARTIDA - (pygame.time.get_ticks() - inicio_partida) // 1000

    # Captura eventos como fechar a janela ou apertar uma tecla.
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Quando a partida termina, ESPAÇO começa uma nova partida.
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE and tempo_restante <= 0:
            pontos_p1 = 0
            pontos_p2 = 0
            reiniciar_posicoes()
            inicio_partida = pygame.time.get_ticks()

    # Verifica quais teclas estão pressionadas neste momento.
    teclas = pygame.key.get_pressed()
    
    # Se o tempo acabou, mostra o resultado e não permite novos movimentos.
    if tempo_restante <= 0:
        tela.fill(GRAMADO)
        # Começamos considerando empate. Depois verificamos quem fez mais gols.
        resultado = "EMPATE!"
        if pontos_p1 > pontos_p2:
            resultado = "JOGADOR 1 VENCEU!"
        elif pontos_p2 > pontos_p1:
            resultado = "JOGADOR 2 VENCEU!"

        texto_resultado = fonte.render(resultado, True, COR_TEXTO)
        tela.blit(texto_resultado, (LARGURA // 2 - texto_resultado.get_width() // 2, ALTURA // 2 - 50))

        texto_final = fonte.render(f"{pontos_p1}   x   {pontos_p2}", True, COR_TEXTO)
        tela.blit(texto_final, (LARGURA // 2 - texto_final.get_width() // 2, ALTURA // 2 + 10))

        texto_reinicio = fonte.render("PARA OUTRA PARTIDA PRESSIONE ESPAÇO", True, COR_TEXTO)
        tela.blit(texto_reinicio, (LARGURA // 2 - texto_reinicio.get_width() // 2, ALTURA // 2 + 70))

        pygame.display.flip()
        continue

    # Atualiza os jogadores e a bola.
    # Depois verifica as colisões da bola com os jogadores.
    p1.mover(teclas)
    p2.mover(teclas)
    bola.mover()
    
    bola.colidir_jogador(p1)
    bola.colidir_jogador(p2)

    # A bola só marca gol se sair pela esquerda/direita dentro da abertura da trave.
    if bola.x < 0 and Y_TRAVE_CIMA <= bola.y <= Y_TRAVE_BAIXO:
        pontos_p2 += 1
        reiniciar_posicoes()
    elif bola.x > LARGURA and Y_TRAVE_CIMA <= bola.y <= Y_TRAVE_BAIXO:
        pontos_p1 += 1
        reiniciar_posicoes()

    # Tudo que aparece na tela é desenhado nesta parte.
    tela.fill(GRAMADO)
    
    # Desenha a linha central e o círculo do meio do campo.
    pygame.draw.line(tela, LINHA, (LARGURA // 2, 0), (LARGURA // 2, ALTURA), 3)
    pygame.draw.circle(tela, LINHA, (LARGURA // 2, ALTURA // 2), 100, 3)
    
    # Desenha as duas traves.
    pygame.draw.rect(tela, TRAVE, (0, Y_TRAVE_CIMA, 10, ALTURA_TRAVE))
    pygame.draw.rect(tela, TRAVE, (LARGURA - 10, Y_TRAVE_CIMA, 10, ALTURA_TRAVE))

    # Desenha os jogadores e a bola.
    p1.desenhar()
    p2.desenhar()
    bola.desenhar()

    # Mostra a quantidade de gols de cada jogador.
    texto_placar = fonte.render(f"{pontos_p1}   x   {pontos_p2}", True, COR_TEXTO)
    tela.blit(texto_placar, (LARGURA // 2 - texto_placar.get_width() // 2, 20))

    # Converte os segundos restantes para o formato minutos:segundos.
    minutos = tempo_restante // 60
    segundos = tempo_restante % 60
    texto_tempo = fonte.render(f"{minutos}:{segundos:02d}", True, COR_TEXTO)
    tela.blit(texto_tempo, (LARGURA // 2 - texto_tempo.get_width() // 2, 65))

    # Atualiza a janela com tudo que foi desenhado.
    # tick mantém o jogo próximo de 60 FPS.
    pygame.display.flip()
    relogio.tick(FPS)