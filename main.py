import pygame
import random

pygame.init()

pygame.display.set_caption("Python Snake Game")
largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

preta = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

tamanho_do_quadrado = 20
velocidade_atualizacao_jogo = 10

def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_do_quadrado) / tamanho_do_quadrado) * tamanho_do_quadrado
    comida_y = round(random.randrange(0, altura - tamanho_do_quadrado) / tamanho_do_quadrado) * tamanho_do_quadrado
    return comida_x, comida_y


def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])


def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho])


def desenhar_pontuacao(pontos):
    fonte = pygame.font.SysFont("comicsans", 25)
    texto = fonte.render(f"Pontuação: {pontos}", True, branca)
    tela.blit(texto, [1, 1])


def selecionar_velocidade(tecla):
    if tecla == pygame.K_LEFT:
        velocidade_x = -tamanho_do_quadrado
        velocidade_y = 0
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_do_quadrado
        velocidade_y = 0
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = -tamanho_do_quadrado
    elif tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_do_quadrado
    return velocidade_x, velocidade_y


def run_game():
    end_game = False

    x = largura / 2
    y = altura / 2

    velocidade_x = 0
    velocidade_y = 0

    tamanha_cobra = 1
    pixels = []
    
    comida_x, comida_y = gerar_comida()

    while not end_game:
        tela.fill(preta)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game = True
            elif event.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(event.key)

        desenhar_comida(tamanho_do_quadrado, comida_x, comida_y)

        x += velocidade_x
        y += velocidade_y

        if x < 0 or x >= largura or y < 0 or y >= altura:
            end_game = True
        
        if x == comida_x and y == comida_y:
            tamanha_cobra += 1
            comida_x, comida_y = gerar_comida()

        relogio.tick(velocidade_atualizacao_jogo)

        pixels.append([x, y])
        if len(pixels) > tamanha_cobra:
            del pixels[0]

        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                end_game = True

        desenhar_cobra(tamanho_do_quadrado, pixels)
        desenhar_pontuacao(tamanha_cobra - 1)
        pygame.display.update()

    fonte = pygame.font.SysFont("comicsans", 50)
    mensagem = fonte.render("Game Over", True, vermelha)
    tela.blit(mensagem, [largura / 4, altura / 2])
    pygame.display.update()
    
run_game()