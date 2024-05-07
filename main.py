import pygame
import random

pygame.init()

# Definições da tela
largura_tela = 800
altura_tela = 600
tamanho_bloco = 20
FPS = 9

# Definições das cores
branco = (255, 255, 255)
preto = (0, 0, 0)
verde = (0, 255, 0)
vermelho = (255, 0, 0)

# Inicialização da tela
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Jogo da Cobrinha')
relogio = pygame.time.Clock()

# Função para desenhar a cobra na tela
def desenhar_cobra(lista_cobra):
    for segmento in lista_cobra:
        pygame.draw.rect(tela, verde, [segmento[0], segmento[1], tamanho_bloco, tamanho_bloco])

# Função para exibir mensagem na tela
def mensagem(msg, cor):
    fonte = pygame.font.SysFont(None, 25)
    texto = fonte.render(msg, True, cor)
    tela.blit(texto, [largura_tela / 2 - texto.get_width() / 2, altura_tela / 2 - texto.get_height() / 2])

# Função principal do jogo
def jogo():
    jogo_ativo = True
    game_over = False

    # Posição inicial da cobra
    posicao_x = largura_tela / 2
    posicao_y = altura_tela / 2
    delta_x = 0
    delta_y = 0

    # Lista que armazena o corpo da cobra
    lista_cobra = []
    comprimento_cobra = 1

    # Posição inicial da comida
    comida_x = round(random.randrange(0, largura_tela - tamanho_bloco) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura_tela - tamanho_bloco) / 20.0) * 20.0

    while jogo_ativo:
        while game_over:
            tela.fill(branco)
            mensagem("Game Over! Pressione C para jogar novamente ou Q para sair.", vermelho)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        jogo_ativo = False
                        game_over = False
                    if event.key == pygame.K_c:
                        jogo()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogo_ativo = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    delta_x = -tamanho_bloco
                    delta_y = 0
                elif event.key == pygame.K_RIGHT:
                    delta_x = tamanho_bloco
                    delta_y = 0
                elif event.key == pygame.K_UP:
                    delta_x = 0
                    delta_y = -tamanho_bloco
                elif event.key == pygame.K_DOWN:
                    delta_x = 0
                    delta_y = tamanho_bloco

        if posicao_x >= largura_tela or posicao_x < 0 or posicao_y >= altura_tela or posicao_y < 0:
            game_over = True

        posicao_x += delta_x
        posicao_y += delta_y
        tela.fill(preto)
        pygame.draw.rect(tela, vermelho, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])
        cabeca_cobra = []
        cabeca_cobra.append(posicao_x)
        cabeca_cobra.append(posicao_y)
        lista_cobra.append(cabeca_cobra)
        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]

        for segmento in lista_cobra[:-1]:
            if segmento == cabeca_cobra:
                game_over = True

        desenhar_cobra(lista_cobra)
        pygame.display.update()

        if posicao_x == comida_x and posicao_y == comida_y:
            comida_x = round(random.randrange(0, largura_tela - tamanho_bloco) / 20.0) * 20.0
            comida_y = round(random.randrange(0, altura_tela - tamanho_bloco) / 20.0) * 20.0
            comprimento_cobra += 1

        relogio.tick(FPS)

    pygame.quit()
    quit()

jogo()
