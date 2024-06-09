import pygame
import random
import time

def menu(width, height, title):

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(title)
    fundo = pygame.image.load('imagem/bg.png').convert_alpha()
    fundo = pygame.transform.scale(fundo, (width, height))
    rodando = True

    # Carregar fonte para os botões
    fonte_botoes = pygame.font.Font(None, 35)

    sair = False  # Variável para controlar o retorno da função

    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sair = True  # Sair corretamente do jogo

            # Verificar se algum botão foi pressionado
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                posicao_mouse = pygame.mouse.get_pos()

                if botao_iniciar.collidepoint(posicao_mouse):
                    tipo_jogador = escolher_tipo_jogador(width, height, screen)
                    if tipo_jogador is not None:
                        jogador1 = obter_nome_jogador(width, height, screen, 1)
                        if tipo_jogador == 1:
                            jogador2 = obter_nome_jogador(width, height, screen, 2)
                            jogar_semaforo(jogador1, jogador2, screen, width, height)  # Passa os nomes dos jogadores para iniciar o jogo
                            break
                        else:
                            jogador2 = "Bot"
                            if tipo_jogador == 2:
                                jogar_semaforo_bot(jogador1, jogador2, screen, width, height, pontos_1=None, pontos_2=None)
                                break
                            elif tipo_jogador == 3:
                                jogar_bot_medio(jogador1, jogador2, screen, width, height, pontos_1=None, pontos_2=None)
                                break
                            elif tipo_jogador == 4:
                                jogar_bot_dificil(jogador1, jogador2, screen, width, height, pontos_1=None, pontos_2=None)
                                break

                elif botao_sair.collidepoint(posicao_mouse):
                    pygame.quit()
                    sair = True

                elif botao_regras.collidepoint(posicao_mouse):
                    regras(width, height, screen)

        screen.blit(fundo, (0, 0))

        # Definir área dos botões
        botao_iniciar = pygame.Rect(width // 2 - 175, 610, 200, 50)
        texto_iniciar = fonte_botoes.render("Iniciar jogo", True, (255, 255, 255))

        botao_regras = pygame.Rect(width // 2 - -75, 610, 200, 50)
        texto_regras = fonte_botoes.render("Regras do jogo", True, (255, 255, 255))

        botao_sair = pygame.Rect(width // 2 - -325, 610, 200, 50)
        texto_sair = fonte_botoes.render("Sair", True, (255, 255, 255))

        # Desenhar os botões na tela
        pygame.draw.rect(screen, (0, 0, 0), botao_iniciar)
        screen.blit(texto_iniciar, (botao_iniciar.centerx - texto_iniciar.get_width() // 2, botao_iniciar.centery - texto_iniciar.get_height() // 2))

        pygame.draw.rect(screen, (0, 0, 0), botao_regras)
        screen.blit(texto_regras, (botao_regras.centerx - texto_regras.get_width() // 2, botao_regras.centery - texto_regras.get_height() // 2))

        pygame.draw.rect(screen, (0, 0, 0), botao_sair)
        screen.blit(texto_sair, (botao_sair.centerx - texto_sair.get_width() // 2, botao_sair.centery - texto_sair.get_height() // 2))

        pygame.display.flip()

    pygame.quit()
    return sair

def escolher_tipo_jogador(width, height, screen):

    fundo = pygame.image.load('imagem/bg1.png').convert_alpha()
    fundo = pygame.transform.scale(fundo, (width, height))
    rodando = True
    tipo_jogador = None

    # Definir fonte do texto
    fonte_texto = pygame.font.Font(None, 36)
    fonte_botoes = pygame.font.Font(None, 36)

    # Definir área dos botões
    botao_jogador1vsjogador2 = pygame.Rect(width // 2 - 150, height // 2 - 20, 300, 50)
    botao_jogador1vsbot = pygame.Rect(width // 2 - 150, height // 2 + 60, 300, 50)
    botao_bot_medio = pygame.Rect(width // 2 - 150, height // 2 + 140, 300, 50)
    botao_bot_dificil = pygame.Rect(width // 2 - 150, height // 2 + 220, 300, 50)
    botao_menu = pygame.Rect(width // 2 - -411, 643, 150, 50)
    texto_menu = fonte_botoes.render("Menu", True, (255, 255, 255))

    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if botao_jogador1vsjogador2.collidepoint(pos):
                    tipo_jogador = 1
                    rodando = False
                elif botao_jogador1vsbot.collidepoint(pos):
                    tipo_jogador = 2
                    rodando = False
                elif botao_bot_medio.collidepoint(pos):
                    tipo_jogador = 3
                    rodando = False
                elif botao_bot_dificil.collidepoint(pos):
                    tipo_jogador = 4
                    rodando = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if botao_menu.collidepoint(event.pos):
                    rodando = False
                    menu(width, height, title)

        # Preencher a tela com o fundo
        screen.blit(fundo, (0, 0))

        # Desenhar o texto na tela
        texto1 = fonte_texto.render("Escolha o tipo de jogador:", True, (255, 255, 255))
        screen.blit(texto1, (width // 2 - texto1.get_width() // 2, height // 2 - 60))

        # Desenhar botões na tela
        pygame.draw.rect(screen, (0, 128, 0), botao_jogador1vsjogador2)
        pygame.draw.rect(screen, (0, 0, 128), botao_jogador1vsbot)
        pygame.draw.rect(screen, (0, 0, 0), botao_menu)
        screen.blit(texto_menu, (botao_menu.centerx - texto_menu.get_width() // 2, botao_menu.centery - texto_menu.get_height() // 2))

        # Desenhar texto nos botões
        texto2 = fonte_texto.render("Local", True, (255, 255, 255))
        texto3 = fonte_texto.render("Bot Fácil", True, (255, 255, 255))
        screen.blit(texto2, (width // 2 - texto2.get_width() // 2, height // 2 - 20 + 10))
        screen.blit(texto3, (width // 2 - texto3.get_width() // 2, height // 2 + 60 + 10))
        pygame.draw.rect(screen, (128, 128, 0), botao_bot_medio)
        pygame.draw.rect(screen, (128, 0, 0), botao_bot_dificil)

        texto4 = fonte_texto.render("Bot Médio", True, (255, 255, 255))
        texto5 = fonte_texto.render("Bot Difícil", True, (255, 255, 255))
        screen.blit(texto4, (width // 2 - texto4.get_width() // 2, height // 2 + 140 + 10))
        screen.blit(texto5, (width // 2 - texto5.get_width() // 2, height // 2 + 220 + 10))

        pygame.display.flip()

    return tipo_jogador

def obter_nome_jogador(width, height, screen, tipo_jogador):

    fundo = pygame.image.load('imagem/bg1.png').convert_alpha()
    fundo = pygame.transform.scale(fundo, (width, height))
    rodando = True
    nome_jogador = ""

    # Definir fonte do texto
    fonte_texto = pygame.font.Font(None, 36)

    # Definir área do campo de texto
    campo_texto = pygame.Rect(width // 2 - 200, height // 2 - 20, 400, 50)

    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    rodando = False
                elif event.key == pygame.K_BACKSPACE:
                    nome_jogador = nome_jogador[:-1]
                else:
                    nome_jogador += event.unicode

        # Preencher a tela com o fundo
        screen.blit(fundo, (0, 0))

        # Desenhar o texto na tela
        if tipo_jogador == 1:
            texto = fonte_texto.render("Digite o nome do Jogador " + str(tipo_jogador) + ":", True, (255, 255, 255))
        else:
            texto = fonte_texto.render("Digite o nome do Jogador:", True, (255, 255, 255))
        screen.blit(texto, (width // 2 - texto.get_width() // 2, height // 2 - 60))

        # Desenhar o campo de texto na tela
        pygame.draw.rect(screen, (255, 255, 255), campo_texto, 2)
        texto_nome = fonte_texto.render(nome_jogador, True, (255, 255, 255))
        screen.blit(texto_nome, (campo_texto.x + 5, campo_texto.y + 5))

        pygame.display.flip()

    return nome_jogador

def fazer_jogada(tabuleiro, linha, coluna):
    if linha < 0 or linha >= len(tabuleiro) or coluna < 0 or coluna >= len(tabuleiro[0]):
        print("Posição inválida no tabuleiro.")
        return False

    if tabuleiro[linha][coluna] == 3:
        print("Esta casa do tabuleiro já não tem mais jogadas possíveis, tente outra vez.")
        return False

    movimento_possível = False
    while not movimento_possível:
        if tabuleiro[linha][coluna] == 1:
            tabuleiro[linha][coluna] = 2
            movimento_possível = True
            break
        elif tabuleiro[linha][coluna] == 2:
            tabuleiro[linha][coluna] = 3
            movimento_possível = True
            break
        else:
            tabuleiro[linha][coluna] = 1
            movimento_possível = True
            break

    return True

def verificar_vencedor(tabuleiro):

    for l in range(3):
        if tabuleiro[l][0] == tabuleiro[l][1] == tabuleiro[l][2] != 0:
            return True
    for l in range(3):
        if tabuleiro[l][1] == tabuleiro[l][2] == tabuleiro[l][3] != 0:
            return True

    for c in range(4):
        if tabuleiro[0][c] == tabuleiro[1][c] == tabuleiro[2][c] != 0:
            return True

    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != 0:
        return True

    if tabuleiro[0][1] == tabuleiro[1][2] == tabuleiro[2][3] != 0:
        return True

    if tabuleiro[0][3] == tabuleiro[1][2] == tabuleiro[2][1] != 0:
        return True

    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != 0:
        return True

    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != 0:
        return True
    return False

def pontos_a_zero():

    pontos_1 = 0
    pontos_2 = 0
    return pontos_1, pontos_2

def atualizar_pontuacao(pontos_1, pontos_2, fonte_pontuacao, jogador1, jogador2):

    texto_pontuacao1 = fonte_pontuacao.render(str(jogador1)+": " + str(pontos_1), True, (255, 255, 255))
    texto_pontuacao2 = fonte_pontuacao.render(str(jogador2)+": " + str(pontos_2), True, (255, 255, 255))
    return texto_pontuacao1, texto_pontuacao2

def somar_pontos(jogador, pontos_1, pontos_2):

    if jogador == 1:
        pontos_1 += 1
    elif jogador == 2:
        pontos_2 += 1
    return pontos_1, pontos_2

def alternar_jogador(jogador_atual):

    if jogador_atual == 1:
        return 2
    else:
        return 1

def jogar_outra_vez(tela):

    fonte = pygame.font.SysFont(None, 30)
    cor_texto = (255, 255, 255)  # branco
    cor_botao_sim = (0, 255, 0)  # verde
    cor_botao_nao = (255, 0, 0)  # vermelho

    largura_botao = 100
    altura_botao = 50
    posicao_botao_sim = (100, 200)
    posicao_botao_nao = (300, 200)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                posicao_mouse = pygame.mouse.get_pos()
                if posicao_botao_sim[0] <= posicao_mouse[0] <= posicao_botao_sim[0] + largura_botao and \
                        posicao_botao_sim[1] <= posicao_mouse[1] <= posicao_botao_sim[1] + altura_botao:
                    return True
                elif posicao_botao_nao[0] <= posicao_mouse[0] <= posicao_botao_nao[0] + largura_botao and \
                        posicao_botao_nao[1] <= posicao_mouse[1] <= posicao_botao_nao[1] + altura_botao:
                    return False

        tela.fill((0, 0, 0))  # Limpa a tela

        # Desenha os botões
        pygame.draw.rect(tela, cor_botao_sim, (*posicao_botao_sim, largura_botao, altura_botao))
        pygame.draw.rect(tela, cor_botao_nao, (*posicao_botao_nao, largura_botao, altura_botao))

        # Desenha o texto nos botões
        texto_sim = fonte.render("Sim", True, cor_texto)
        texto_nao = fonte.render("Não", True, cor_texto)
        tela.blit(texto_sim, (posicao_botao_sim[0] + 20, posicao_botao_sim[1] + 15))
        tela.blit(texto_nao, (posicao_botao_nao[0] + 20, posicao_botao_nao[1] + 15))

        pygame.display.flip()

def quem_joga(fonte_jogadores, jogador_atual):
    if jogador_atual == 1:
        jogador = fonte_jogadores.render(str(jogador_atual)+": ")
    elif jogador_atual == 2:
        jogador = fonte_jogadores.render(str(jogador_atual)+": ")
    return jogador, fonte_jogadores

def desenhar_tabuleiro(tabuleiro, largura_celula, screen, fundo, posicao_tabuleiro, width, altura_texto_pontuacao, altura_texto_jogador, largura_texto_pontuacao1, largura_texto_pontuacao2, largura_texto_jogador1, largura_texto_jogador2, texto_pontuacao1, texto_pontuacao2, texto_jogador1, texto_jogador2, altura_tabuleiro, largura_tabuleiro):
    
    screen.blit(fundo, (0, 0))
    screen.blit(texto_pontuacao1, (width - largura_texto_pontuacao1 - 10, 10))
    screen.blit(texto_pontuacao2, (width - largura_texto_pontuacao2 - 10, 10 + altura_texto_pontuacao + 5))
    screen.blit(texto_jogador1, (width - largura_texto_jogador1 - 10, 10 + altura_texto_pontuacao * 2))
    screen.blit(texto_jogador2, (width - largura_texto_jogador2 - 10, 10 + altura_texto_pontuacao * 3 + altura_texto_jogador))
 #   screen.blit(fundo, posicao_tabuleiro)

    for linha in range(altura_tabuleiro):
        for coluna in range(largura_tabuleiro):
            cor = (255, 255, 255)  # cor padrão para células vazias
            if tabuleiro[linha][coluna] == 1:
                cor = (0, 255, 0)
            elif tabuleiro[linha][coluna] == 2:
                cor = (255, 255, 0)  # cor para células amarelas
            elif tabuleiro[linha][coluna] == 3:
                cor = (255, 0, 0)  # cor para células vermelhas

            pygame.draw.rect(screen, cor, (posicao_tabuleiro[0] + coluna * largura_celula, posicao_tabuleiro[1] + linha * largura_celula, largura_celula-1, largura_celula-1))

    pygame.display.flip()

def escolha():
    num = random.randint(0, 1)
    return num

def jogar_semaforo(jogador1, jogador2, screen, width, height, pontos_1=None, pontos_2=None):
    pygame.init()

    fundo = pygame.image.load('imagem/bg1.png').convert_alpha()
    fundo = pygame.transform.scale(fundo, (width, height))
    rodando = True

    if pontos_1 is None:
        pontos_1 = 0
    if pontos_2 is None:
        pontos_2 = 0

    # carregar fonte para os botões
    fonte_botoes = pygame.font.Font(None, 35)
    fonte_jogadores = pygame.font.Font(None, 25)
    fonte_pontuacao = pygame.font.Font(None, 30)

    pontos_a_zero()

    texto_pontuacao1, texto_pontuacao2 = atualizar_pontuacao(pontos_1, pontos_2, fonte_pontuacao, jogador1, jogador2)

    largura_texto_pontuacao1 = texto_pontuacao1.get_width()
    largura_texto_pontuacao2 = texto_pontuacao2.get_width()
    altura_texto_pontuacao = texto_pontuacao1.get_height()

    texto_jogador1 = fonte_jogadores.render(f"", True, (255, 255, 255))
    texto_jogador2 = fonte_jogadores.render(f"", True, (255, 255, 255))
    largura_texto_jogador1 = texto_jogador1.get_width()
    largura_texto_jogador2 = texto_jogador2.get_width()
    altura_texto_jogador = texto_jogador1.get_height()

    # definir área dos botões
    botao_menu = pygame.Rect(width // 2 - -411, 645, 150, 50)
    texto_menu = fonte_botoes.render("menu", True, (255, 255, 255))

    num_linhas = 3
    num_colunas = 4

    # Definição do tamanho dos quadrados do tabuleiro
    largura_quadrado = width // num_colunas
    altura_quadrado = height // num_linhas

    print("Iniciando jogo...")
    print("Jogador 1:", jogador1)
    print("Jogador 2:", jogador2)

    tabuleiro = [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]]

    largura_celula = 150  # Ajuste para o tamanho das células do tabuleiro
    largura_tabuleiro = len(tabuleiro[0])
    altura_tabuleiro = len(tabuleiro)
    tamanho_tabuleiro = (largura_tabuleiro * largura_celula, altura_tabuleiro * largura_celula)
    posicao_tabuleiro = ((width - tamanho_tabuleiro[0]) // 2 - 200, (height - tamanho_tabuleiro[1]) // 2)  # Ajuste a posição x para deslocar o tabuleiro para a esquerda
    tela = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Jogo do Semáforo")
    desenhar_tabuleiro(tabuleiro, largura_celula, screen, fundo, posicao_tabuleiro, width, altura_texto_pontuacao, altura_texto_jogador, largura_texto_pontuacao1, largura_texto_pontuacao2, largura_texto_jogador1, largura_texto_jogador2, texto_pontuacao1, texto_pontuacao2, texto_jogador1, texto_jogador2, altura_tabuleiro, largura_tabuleiro)
    jogador_atual = 1 #random.randint(1, 2)

    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

            # Verifica se algum botão foi pressionado
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                posicao_mouse = pygame.mouse.get_pos()
                if posicao_tabuleiro[0] <= posicao_mouse[0] < posicao_tabuleiro[0] + tamanho_tabuleiro[0] and posicao_tabuleiro[1] <= posicao_mouse[1] < posicao_tabuleiro[1] + tamanho_tabuleiro[1]:
                    coluna_clicada = (posicao_mouse[0] - posicao_tabuleiro[0]) // largura_celula
                    linha_clicada = (posicao_mouse[1] - posicao_tabuleiro[1]) // largura_celula
                    if linha_clicada < altura_tabuleiro and coluna_clicada < largura_tabuleiro:
                        if fazer_jogada(tabuleiro, linha_clicada, coluna_clicada):
                            desenhar_tabuleiro(tabuleiro, largura_celula, screen, fundo, posicao_tabuleiro, width, altura_texto_pontuacao, altura_texto_jogador, largura_texto_pontuacao1, largura_texto_pontuacao2, largura_texto_jogador1, largura_texto_jogador2, texto_pontuacao1, texto_pontuacao2, texto_jogador1, texto_jogador2, altura_tabuleiro, largura_tabuleiro)
                            time.sleep(0.5)

                            if verificar_vencedor(tabuleiro):
                                print('Jogador', jogador_atual, 'venceu!')
                                # Atualiza a pontuação dos jogadores
                                pontos_1, pontos_2 = somar_pontos(jogador_atual, pontos_1, pontos_2)

                                # Atualiza o texto da pontuação na tela
                                texto_pontuacao1, texto_pontuacao2 = atualizar_pontuacao(pontos_1, pontos_2, fonte_pontuacao, jogador1, jogador2)

                                tabuleiro = [[0, 0, 0, 0],
                                             [0, 0, 0, 0],
                                             [0, 0, 0, 0]]
                                jogador_atual = 1
                                # Atualiza o texto da pontuação
                                screen.blit(fundo, (0, 0))
                                screen.blit(texto_pontuacao1, (width - largura_texto_pontuacao1 - 10, 10))
                                screen.blit(texto_pontuacao2, (width - largura_texto_pontuacao2 - 10, 10 + altura_texto_pontuacao + 5))
                                pygame.display.flip()

                                time.sleep(0.5)   # Adicionar um atraso de 0.5 segundo aqui
                                
                                desenhar_tabuleiro(tabuleiro, largura_celula, screen, fundo, posicao_tabuleiro, width, altura_texto_pontuacao, altura_texto_jogador, largura_texto_pontuacao1, largura_texto_pontuacao2, largura_texto_jogador1, largura_texto_jogador2, texto_pontuacao1, texto_pontuacao2, texto_jogador1, texto_jogador2, altura_tabuleiro, largura_tabuleiro)

                                continue

                            jogador_atual = alternar_jogador(jogador_atual)

                # Verifica se o botão Menu foi clicado
                if botao_menu.collidepoint(event.pos):
                    rodando = False
                    menu(width, height, title)

        pygame.draw.rect(screen, (0, 0, 0), botao_menu)
        screen.blit(texto_menu, (botao_menu.centerx - texto_menu.get_width() // 2, botao_menu.centery - texto_menu.get_height() // 2))
        pygame.display.flip()

    pygame.quit()

def jogar_semaforo_bot(jogador1, jogador2, screen, width, height, pontos_1=None, pontos_2=None):
    pygame.init()

    fundo = pygame.image.load('imagem/bg1.png').convert_alpha()
    fundo = pygame.transform.scale(fundo, (width, height))
    rodando = True

    if pontos_1 is None:
        pontos_1 = 0
    if pontos_2 is None:
        pontos_2 = 0

    # carregar fonte para os botões
    fonte_botoes = pygame.font.Font(None, 35)
    fonte_jogadores = pygame.font.Font(None, 25)
    fonte_pontuacao = pygame.font.Font(None, 30)

    pontos_a_zero()

    texto_pontuacao1, texto_pontuacao2 = atualizar_pontuacao(pontos_1, pontos_2, fonte_pontuacao, jogador1, jogador2)

    largura_texto_pontuacao1 = texto_pontuacao1.get_width()
    largura_texto_pontuacao2 = texto_pontuacao2.get_width()
    altura_texto_pontuacao = texto_pontuacao1.get_height()

    texto_jogador1 = fonte_jogadores.render(f"", True, (255, 255, 255))
    texto_jogador2 = fonte_jogadores.render(f"", True, (255, 255, 255))
    largura_texto_jogador1 = texto_jogador1.get_width()
    largura_texto_jogador2 = texto_jogador2.get_width()
    altura_texto_jogador = texto_jogador1.get_height()

    # definir área dos botões
    botao_menu = pygame.Rect(width // 2 - -411, 645, 150, 50)
    texto_menu = fonte_botoes.render("Menu", True, (255, 255, 255))

    num_linhas = 3
    num_colunas = 4

    # Definição do tamanho dos quadrados do tabuleiro
    largura_quadrado = width // num_colunas
    altura_quadrado = height // num_linhas

    tabuleiro = [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]]

    largura_celula = 150  # Ajuste para o tamanho das células do tabuleiro
    largura_tabuleiro = len(tabuleiro[0])
    altura_tabuleiro = len(tabuleiro)
    tamanho_tabuleiro = (largura_tabuleiro * largura_celula, altura_tabuleiro * largura_celula)
    posicao_tabuleiro = ((width - tamanho_tabuleiro[0]) // 2 - 200, (height - tamanho_tabuleiro[1]) // 2)  # Ajuste a posição x para deslocar o tabuleiro para a esquerda
    tela = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Jogo do Semáforo")
    desenhar_tabuleiro(tabuleiro, largura_celula, screen, fundo, posicao_tabuleiro, width, altura_texto_pontuacao, altura_texto_jogador, largura_texto_pontuacao1, largura_texto_pontuacao2, largura_texto_jogador1, largura_texto_jogador2, texto_pontuacao1, texto_pontuacao2, texto_jogador1, texto_jogador2, altura_tabuleiro, largura_tabuleiro)
    jogador_atual = 1

    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

            # Verifica se algum botão foi pressionado
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                posicao_mouse = pygame.mouse.get_pos()
                if posicao_tabuleiro[0] <= posicao_mouse[0] < posicao_tabuleiro[0] + tamanho_tabuleiro[0] and posicao_tabuleiro[1] <= posicao_mouse[1] < posicao_tabuleiro[1] + tamanho_tabuleiro[1]:
                    coluna_clicada = (posicao_mouse[0] - posicao_tabuleiro[0]) // largura_celula
                    linha_clicada = (posicao_mouse[1] - posicao_tabuleiro[1]) // largura_celula
                    if linha_clicada < altura_tabuleiro and coluna_clicada < largura_tabuleiro:
                        if jogador_atual == 1:
                            if fazer_jogada(tabuleiro, linha_clicada, coluna_clicada):
                                desenhar_tabuleiro(tabuleiro, largura_celula, screen, fundo, posicao_tabuleiro, width, altura_texto_pontuacao, altura_texto_jogador, largura_texto_pontuacao1, largura_texto_pontuacao2, largura_texto_jogador1, largura_texto_jogador2, texto_pontuacao1, texto_pontuacao2, texto_jogador1, texto_jogador2, altura_tabuleiro, largura_tabuleiro)
                                time.sleep(0.5)

                                if verificar_vencedor(tabuleiro):
                                    print('Jogador', jogador_atual, 'venceu!')
                                    # Atualiza a pontuação dos jogadores
                                    pontos_1, pontos_2 = somar_pontos(jogador_atual, pontos_1, pontos_2)

                                    # Atualiza o texto da pontuação na tela
                                    texto_pontuacao1, texto_pontuacao2 = atualizar_pontuacao(pontos_1, pontos_2, fonte_pontuacao, jogador1, jogador2)

                                    tabuleiro = [[0, 0, 0, 0],
                                                [0, 0, 0, 0],
                                                [0, 0, 0, 0]]
                                    jogador_atual = 1
                                    # Atualiza o texto da pontuação
                                    screen.blit(fundo, (0, 0))
                                    screen.blit(texto_pontuacao1, (width - largura_texto_pontuacao1 - 10, 10))
                                    screen.blit(texto_pontuacao2, (width - largura_texto_pontuacao2 - 10, 10 + altura_texto_pontuacao + 5))
                                    pygame.display.flip()

                                    time.sleep(0.5)   # Adicionar um atraso de 1 segundo aqui
                                    
                                    desenhar_tabuleiro(tabuleiro, largura_celula, screen, fundo, posicao_tabuleiro, width, altura_texto_pontuacao, altura_texto_jogador, largura_texto_pontuacao1, largura_texto_pontuacao2, largura_texto_jogador1, largura_texto_jogador2, texto_pontuacao1, texto_pontuacao2, texto_jogador1, texto_jogador2, altura_tabuleiro, largura_tabuleiro)

                                    continue

                                jogador_atual = alternar_jogador(jogador_atual)
                        
                        elif jogador_atual == 2:
                            linha_clicada = random.randint(0, 2)
                            coluna_clicada = random.randint(0, 3)
                            if fazer_jogada(tabuleiro, linha_clicada, coluna_clicada):
                                desenhar_tabuleiro(tabuleiro, largura_celula, screen, fundo, posicao_tabuleiro, width, altura_texto_pontuacao, altura_texto_jogador, largura_texto_pontuacao1, largura_texto_pontuacao2, largura_texto_jogador1, largura_texto_jogador2, texto_pontuacao1, texto_pontuacao2, texto_jogador1, texto_jogador2, altura_tabuleiro, largura_tabuleiro)
                                time.sleep(1)

                                if verificar_vencedor(tabuleiro):
                                    print('Jogador', jogador_atual, 'venceu!')
                                    # Atualiza a pontuação dos jogadores
                                    pontos_1, pontos_2 = somar_pontos(jogador_atual, pontos_1, pontos_2)

                                    # Atualiza o texto da pontuação na tela
                                    texto_pontuacao1, texto_pontuacao2 = atualizar_pontuacao(pontos_1, pontos_2, fonte_pontuacao, jogador1, jogador2)

                                    tabuleiro = [[0, 0, 0, 0],
                                                [0, 0, 0, 0],
                                                [0, 0, 0, 0]]
                                    jogador_atual = 1
                                    # Atualiza o texto da pontuação
                                    screen.blit(fundo, (0, 0))
                                    screen.blit(texto_pontuacao1, (width - largura_texto_pontuacao1 - 10, 10))
                                    screen.blit(texto_pontuacao2, (width - largura_texto_pontuacao2 - 10, 10 + altura_texto_pontuacao + 5))
                                    pygame.display.flip()

                                    time.sleep(0.5)   # Adicionar um atraso de 0.5 segundo aqui
                                    
                                    desenhar_tabuleiro(tabuleiro, largura_celula, screen, fundo, posicao_tabuleiro, width, altura_texto_pontuacao, altura_texto_jogador, largura_texto_pontuacao1, largura_texto_pontuacao2, largura_texto_jogador1, largura_texto_jogador2, texto_pontuacao1, texto_pontuacao2, texto_jogador1, texto_jogador2, altura_tabuleiro, largura_tabuleiro)

                                    continue

                                jogador_atual = alternar_jogador(jogador_atual)
                # Verifica se o botão Menu foi clicado
                if botao_menu.collidepoint(event.pos):
                    rodando = False
                    menu(width, height, title)

        pygame.draw.rect(screen, (0, 0, 0), botao_menu)
        screen.blit(texto_menu, (botao_menu.centerx - texto_menu.get_width() // 2, botao_menu.centery - texto_menu.get_height() // 2))
        pygame.display.flip()

    pygame.quit()

def jogar_bot_medio(jogador1, jogador2, screen, width, height, pontos_1=None, pontos_2=None):
    pygame.init()

    fundo = pygame.image.load('imagem/bg1.png').convert_alpha()
    fundo = pygame.transform.scale(fundo, (width, height))
    rodando = True

    if pontos_1 is None:
        pontos_1 = 0
    if pontos_2 is None:
        pontos_2 = 0

    # carregar fonte para os botões
    fonte_botoes = pygame.font.Font(None, 35)
    fonte_jogadores = pygame.font.Font(None, 25)
    fonte_pontuacao = pygame.font.Font(None, 30)

    pontos_a_zero()

    texto_pontuacao1, texto_pontuacao2 = atualizar_pontuacao(pontos_1, pontos_2, fonte_pontuacao, jogador1, jogador2)

    largura_texto_pontuacao1 = texto_pontuacao1.get_width()
    largura_texto_pontuacao2 = texto_pontuacao2.get_width()
    altura_texto_pontuacao = texto_pontuacao1.get_height()

    texto_jogador1 = fonte_jogadores.render(f"", True, (255, 255, 255))
    texto_jogador2 = fonte_jogadores.render(f"", True, (255, 255, 255))
    largura_texto_jogador1 = texto_jogador1.get_width()
    largura_texto_jogador2 = texto_jogador2.get_width()
    altura_texto_jogador = texto_jogador1.get_height()

    # definir área dos botões
    botao_menu = pygame.Rect(width // 2 - -411, 645, 150, 50)
    texto_menu = fonte_botoes.render("Menu", True, (255, 255, 255))

    num_linhas = 3
    num_colunas = 4

    # Definição do tamanho dos quadrados do tabuleiro
    largura_quadrado = width // num_colunas
    altura_quadrado = height // num_linhas

    tabuleiro = [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]]

    largura_celula = 150  # Ajuste para o tamanho das células do tabuleiro
    largura_tabuleiro = len(tabuleiro[0])
    altura_tabuleiro = len(tabuleiro)
    tamanho_tabuleiro = (largura_tabuleiro * largura_celula, altura_tabuleiro * largura_celula)
    posicao_tabuleiro = ((width - tamanho_tabuleiro[0]) // 2 - 200, (height - tamanho_tabuleiro[1]) // 2)  # Ajuste a posição x para deslocar o tabuleiro para a esquerda
    tela = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Jogo do Semáforo")
    desenhar_tabuleiro(tabuleiro, largura_celula, screen, fundo, posicao_tabuleiro, width, altura_texto_pontuacao, altura_texto_jogador, largura_texto_pontuacao1, largura_texto_pontuacao2, largura_texto_jogador1, largura_texto_jogador2, texto_pontuacao1, texto_pontuacao2, texto_jogador1, texto_jogador2, altura_tabuleiro, largura_tabuleiro)
    jogador_atual = 1

    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

            # Verifica se algum botão foi pressionado
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                posicao_mouse = pygame.mouse.get_pos()
                if posicao_tabuleiro[0] <= posicao_mouse[0] < posicao_tabuleiro[0] + tamanho_tabuleiro[0] and posicao_tabuleiro[1] <= posicao_mouse[1] < posicao_tabuleiro[1] + tamanho_tabuleiro[1]:
                    coluna_clicada = (posicao_mouse[0] - posicao_tabuleiro[0]) // largura_celula
                    linha_clicada = (posicao_mouse[1] - posicao_tabuleiro[1]) // largura_celula
                    if linha_clicada < altura_tabuleiro and coluna_clicada < largura_tabuleiro:
                        if jogador_atual == 1:
                            if fazer_jogada(tabuleiro, linha_clicada, coluna_clicada):
                                desenhar_tabuleiro(tabuleiro, largura_celula, screen, fundo, posicao_tabuleiro, width, altura_texto_pontuacao, altura_texto_jogador, largura_texto_pontuacao1, largura_texto_pontuacao2, largura_texto_jogador1, largura_texto_jogador2, texto_pontuacao1, texto_pontuacao2, texto_jogador1, texto_jogador2, altura_tabuleiro, largura_tabuleiro)
                                time.sleep(0.5)

                                if verificar_vencedor(tabuleiro):
                                    print('Jogador', jogador_atual, 'venceu!')
                                    # Atualiza a pontuação dos jogadores
                                    pontos_1, pontos_2 = somar_pontos(jogador_atual, pontos_1, pontos_2)

                                    # Atualiza o texto da pontuação na tela
                                    texto_pontuacao1, texto_pontuacao2 = atualizar_pontuacao(pontos_1, pontos_2, fonte_pontuacao, jogador1, jogador2)

                                    tabuleiro = [[0, 0, 0, 0],
                                                 [0, 0, 0, 0],
                                                 [0, 0, 0, 0]]
                                    jogador_atual = 1
                                    # Atualiza o texto da pontuação
                                    screen.blit(fundo, (0, 0))
                                    screen.blit(texto_pontuacao1, (width - largura_texto_pontuacao1 - 10, 10))
                                    screen.blit(texto_pontuacao2, (width - largura_texto_pontuacao2 - 10, 10 + altura_texto_pontuacao + 5))
                                    pygame.display.flip()

                                    time.sleep(0.5)   # Adicionar um atraso de 0.5 segundo aqui
                                    
                                    desenhar_tabuleiro(tabuleiro, largura_celula, screen, fundo, posicao_tabuleiro, width, altura_texto_pontuacao, altura_texto_jogador, largura_texto_pontuacao1, largura_texto_pontuacao2, largura_texto_jogador1, largura_texto_jogador2, texto_pontuacao1, texto_pontuacao2, texto_jogador1, texto_jogador2, altura_tabuleiro, largura_tabuleiro)

                                    continue

                                jogador_atual = alternar_jogador(jogador_atual)
                        
                        elif jogador_atual == 2:
                            if bot_medio(tabuleiro):
                                desenhar_tabuleiro(tabuleiro, largura_celula, screen, fundo, posicao_tabuleiro, width, altura_texto_pontuacao, altura_texto_jogador, largura_texto_pontuacao1, largura_texto_pontuacao2, largura_texto_jogador1, largura_texto_jogador2, texto_pontuacao1, texto_pontuacao2, texto_jogador1, texto_jogador2, altura_tabuleiro, largura_tabuleiro)
                                time.sleep(1)

                                if verificar_vencedor(tabuleiro):
                                    print('Jogador', jogador_atual, 'venceu!')
                                    # Atualiza a pontuação dos jogadores
                                    pontos_1, pontos_2 = somar_pontos(jogador_atual, pontos_1, pontos_2)

                                    # Atualiza o texto da pontuação na tela
                                    texto_pontuacao1, texto_pontuacao2 = atualizar_pontuacao(pontos_1, pontos_2, fonte_pontuacao, jogador1, jogador2)

                                    tabuleiro = [[0, 0, 0, 0],
                                                 [0, 0, 0, 0],
                                                 [0, 0, 0, 0]]
                                    jogador_atual = 1
                                    # Atualiza o texto da pontuação
                                    screen.blit(fundo, (0, 0))
                                    screen.blit(texto_pontuacao1, (width - largura_texto_pontuacao1 - 10, 10))
                                    screen.blit(texto_pontuacao2, (width - largura_texto_pontuacao2 - 10, 10 + altura_texto_pontuacao + 5))
                                    pygame.display.flip()

                                    time.sleep(0.5)   # Adicionar um atraso de 0.5 segundo aqui
                                    
                                    desenhar_tabuleiro(tabuleiro, largura_celula, screen, fundo, posicao_tabuleiro, width, altura_texto_pontuacao, altura_texto_jogador, largura_texto_pontuacao1, largura_texto_pontuacao2, largura_texto_jogador1, largura_texto_jogador2, texto_pontuacao1, texto_pontuacao2, texto_jogador1, texto_jogador2, altura_tabuleiro, largura_tabuleiro)

                                    continue

                                jogador_atual = alternar_jogador(jogador_atual)
                # Verifica se o botão Menu foi clicado
                if botao_menu.collidepoint(event.pos):
                    rodando = False
                    menu(width, height, title)

        pygame.draw.rect(screen, (0, 0, 0), botao_menu)
        screen.blit(texto_menu, (botao_menu.centerx - texto_menu.get_width() // 2, botao_menu.centery - texto_menu.get_height() // 2))
        pygame.display.flip()

    pygame.quit()

def bot_medio(tabuleiro):
    movimento_encontrado = False

    while not movimento_encontrado:
        for l in range(3):
            for i in range(4):
                if i < 2 and tabuleiro[l][i] == tabuleiro[l][i+1] != 0 and tabuleiro[l][i] == tabuleiro[l][+1] == tabuleiro[l][i+2] + 1 and 0 <= i+2 < 4:
                    fazer_jogada(tabuleiro, l, i+2)
                    movimento_encontrado = True
                    break
                if i < 2 and tabuleiro[l][i] == tabuleiro[l][i+2] != 0 and tabuleiro[l][i] == tabuleiro[l][i+2] == tabuleiro[l][i+1] + 1:
                    fazer_jogada(tabuleiro, l, i+1)
                    movimento_encontrado = True
                    break
                if 2 <= i <= 3 and tabuleiro[l][i] == tabuleiro[l][i-1] != 0 and tabuleiro[l][i] == tabuleiro[l][i-1] == tabuleiro[l][i-2] + 1:
                    fazer_jogada(tabuleiro, l, i-2)
                    movimento_encontrado = True
                    break
                if 2 <= i <= 3 and tabuleiro[l][i] == tabuleiro[l][i-2] != 0 and tabuleiro[l][i] == tabuleiro[l][i-2] == tabuleiro[l][i-1] + 1:
                    fazer_jogada(tabuleiro, l, i-1)
                    movimento_encontrado = True
                    break
            if movimento_encontrado:
                break
        
        if not movimento_encontrado:
            for c in range(4):
                if tabuleiro[0][c] == tabuleiro [1][c] != 0 and tabuleiro[0][c] == tabuleiro [1][c] == tabuleiro[2][c] + 1:
                    fazer_jogada(tabuleiro, 2, c)
                    movimento_encontrado = True
                    break
                if tabuleiro[0][c] == tabuleiro [2][c] != 0 and tabuleiro[0][c] == tabuleiro [2][c] == tabuleiro[1][c] + 1:
                    fazer_jogada(tabuleiro, 1, c)
                    movimento_encontrado = True
                    break
                if tabuleiro[2][c] == tabuleiro [1][c] != 0 and tabuleiro[2][c] == tabuleiro [1][c] == tabuleiro[0][c] + 1:
                    fazer_jogada(tabuleiro, 0, c)
                    movimento_encontrado = True
                    break
            if movimento_encontrado:
                break
        
        if not movimento_encontrado:
            for c in range(4):
                if 0 <= c <= 1 and tabuleiro[0][c] == tabuleiro[1][c+1] != 0 and tabuleiro[0][c] == tabuleiro[1][c+1] == tabuleiro[2][c+2] + 1:
                    fazer_jogada(tabuleiro, 2, c+2)
                    movimento_encontrado = True
                    break
                if 0 <= c <= 1 and tabuleiro[0][c] == tabuleiro[2][c+2] != 0 and tabuleiro[0][c] == tabuleiro[2][c+2] == tabuleiro[1][c+1] + 1:
                    fazer_jogada(tabuleiro, 1, c+1)
                    movimento_encontrado = True
                    break
                if 0 <= c <= 1 and tabuleiro[1][c+1] == tabuleiro[2][c+2] != 0 and tabuleiro[1][c+1] == tabuleiro[2][c+2] == tabuleiro[0][c] + 1:
                    fazer_jogada(tabuleiro, 0, c)
                    movimento_encontrado = True
                    break
                if 2 <= c <= 3 and tabuleiro[0][c] == tabuleiro[1][c-1] != 0 and tabuleiro[0][c] == tabuleiro[1][c-1] == tabuleiro[2][c-2] + 1:
                    fazer_jogada(tabuleiro, 2, c-2)
                    movimento_encontrado = True
                    break
                if 2 <= c <= 3 and tabuleiro[0][c] == tabuleiro[2][c-2] != 0 and tabuleiro[0][c] == tabuleiro[2][c-2] == tabuleiro[1][c-1] + 1:
                    fazer_jogada(tabuleiro, 1, c-1)
                    movimento_encontrado = True
                    break
                if 2 <= c <= 3 and tabuleiro[1][c-1] == tabuleiro[2][c-2] != 0 and tabuleiro[1][c-1] == tabuleiro[2][c-2] == tabuleiro[0][c] + 1:
                    fazer_jogada(tabuleiro, 0, c)
                    movimento_encontrado = True
                    break
            if movimento_encontrado:
                break
    
        if not movimento_encontrado:
            linha = random.randint(0, 2)
            coluna = random.randint(0, 3)

            while tabuleiro[linha][coluna] == 3:
                linha = random.randint(0, 2)
                coluna = random.randint(0, 3)

            fazer_jogada(tabuleiro, linha, coluna)
            movimento_encontrado = True
        
    return movimento_encontrado

def jogar_bot_dificil(jogador1, jogador2, screen, width, height, pontos_1=None, pontos_2=None):
    pygame.init()

    fundo = pygame.image.load('imagem/bg1.png').convert_alpha()
    fundo = pygame.transform.scale(fundo, (width, height))
    rodando = True

    if pontos_1 is None:
        pontos_1 = 0
    if pontos_2 is None:
        pontos_2 = 0

    # carregar fonte para os botões
    fonte_botoes = pygame.font.Font(None, 35)
    fonte_jogadores = pygame.font.Font(None, 25)
    fonte_pontuacao = pygame.font.Font(None, 30)

    pontos_a_zero()

    texto_pontuacao1, texto_pontuacao2 = atualizar_pontuacao(pontos_1, pontos_2, fonte_pontuacao, jogador1, jogador2)

    largura_texto_pontuacao1 = texto_pontuacao1.get_width()
    largura_texto_pontuacao2 = texto_pontuacao2.get_width()
    altura_texto_pontuacao = texto_pontuacao1.get_height()

    texto_jogador1 = fonte_jogadores.render(f"", True, (255, 255, 255))
    texto_jogador2 = fonte_jogadores.render(f"", True, (255, 255, 255))
    largura_texto_jogador1 = texto_jogador1.get_width()
    largura_texto_jogador2 = texto_jogador2.get_width()
    altura_texto_jogador = texto_jogador1.get_height()

    # definir área dos botões
    botao_menu = pygame.Rect(width // 2 - -411, 645, 150, 50)
    texto_menu = fonte_botoes.render("Menu", True, (255, 255, 255))

    num_linhas = 3
    num_colunas = 4

    # Definição do tamanho dos quadrados do tabuleiro
    largura_quadrado = width // num_colunas
    altura_quadrado = height // num_linhas

    tabuleiro = [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]]

    largura_celula = 150  # Ajuste para o tamanho das células do tabuleiro
    largura_tabuleiro = len(tabuleiro[0])
    altura_tabuleiro = len(tabuleiro)
    tamanho_tabuleiro = (largura_tabuleiro * largura_celula, altura_tabuleiro * largura_celula)
    posicao_tabuleiro = ((width - tamanho_tabuleiro[0]) // 2 - 200, (height - tamanho_tabuleiro[1]) // 2)  # Ajuste a posição x para deslocar o tabuleiro para a esquerda
    tela = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Jogo do Semáforo")
    desenhar_tabuleiro(tabuleiro, largura_celula, screen, fundo, posicao_tabuleiro, width, altura_texto_pontuacao, altura_texto_jogador, largura_texto_pontuacao1, largura_texto_pontuacao2, largura_texto_jogador1, largura_texto_jogador2, texto_pontuacao1, texto_pontuacao2, texto_jogador1, texto_jogador2, altura_tabuleiro, largura_tabuleiro)
    jogador_atual = 1

    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

            # Verifica se algum botão foi pressionado
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                posicao_mouse = pygame.mouse.get_pos()
                if posicao_tabuleiro[0] <= posicao_mouse[0] < posicao_tabuleiro[0] + tamanho_tabuleiro[0] and posicao_tabuleiro[1] <= posicao_mouse[1] < posicao_tabuleiro[1] + tamanho_tabuleiro[1]:
                    coluna_clicada = (posicao_mouse[0] - posicao_tabuleiro[0]) // largura_celula
                    linha_clicada = (posicao_mouse[1] - posicao_tabuleiro[1]) // largura_celula
                    if linha_clicada < altura_tabuleiro and coluna_clicada < largura_tabuleiro:
                        if jogador_atual == 1:
                            if fazer_jogada(tabuleiro, linha_clicada, coluna_clicada):
                                desenhar_tabuleiro(tabuleiro, largura_celula, screen, fundo, posicao_tabuleiro, width, altura_texto_pontuacao, altura_texto_jogador, largura_texto_pontuacao1, largura_texto_pontuacao2, largura_texto_jogador1, largura_texto_jogador2, texto_pontuacao1, texto_pontuacao2, texto_jogador1, texto_jogador2, altura_tabuleiro, largura_tabuleiro)
                                time.sleep(0.5)

                                if verificar_vencedor(tabuleiro):
                                    print('Jogador', jogador_atual, 'venceu!')
                                    # Atualiza a pontuação dos jogadores
                                    pontos_1, pontos_2 = somar_pontos(jogador_atual, pontos_1, pontos_2)

                                    # Atualiza o texto da pontuação na tela
                                    texto_pontuacao1, texto_pontuacao2 = atualizar_pontuacao(pontos_1, pontos_2, fonte_pontuacao, jogador1, jogador2)

                                    tabuleiro = [[0, 0, 0, 0],
                                                 [0, 0, 0, 0],
                                                 [0, 0, 0, 0]]
                                    jogador_atual = 1
                                    # Atualiza o texto da pontuação
                                    screen.blit(fundo, (0, 0))
                                    screen.blit(texto_pontuacao1, (width - largura_texto_pontuacao1 - 10, 10))
                                    screen.blit(texto_pontuacao2, (width - largura_texto_pontuacao2 - 10, 10 + altura_texto_pontuacao + 5))
                                    pygame.display.flip()

                                    time.sleep(0.5)   # Adicionar um atraso de 0.5 segundo aqui
                                    
                                    desenhar_tabuleiro(tabuleiro, largura_celula, screen, fundo, posicao_tabuleiro, width, altura_texto_pontuacao, altura_texto_jogador, largura_texto_pontuacao1, largura_texto_pontuacao2, largura_texto_jogador1, largura_texto_jogador2, texto_pontuacao1, texto_pontuacao2, texto_jogador1, texto_jogador2, altura_tabuleiro, largura_tabuleiro)

                                    continue

                                jogador_atual = alternar_jogador(jogador_atual)
                        
                        elif jogador_atual == 2:
                            if bot_dificil(tabuleiro):
                                desenhar_tabuleiro(tabuleiro, largura_celula, screen, fundo, posicao_tabuleiro, width, altura_texto_pontuacao, altura_texto_jogador, largura_texto_pontuacao1, largura_texto_pontuacao2, largura_texto_jogador1, largura_texto_jogador2, texto_pontuacao1, texto_pontuacao2, texto_jogador1, texto_jogador2, altura_tabuleiro, largura_tabuleiro)
                                time.sleep(1)

                                if verificar_vencedor(tabuleiro):
                                    print('Jogador', jogador_atual, 'venceu!')
                                    # Atualiza a pontuação dos jogadores
                                    pontos_1, pontos_2 = somar_pontos(jogador_atual, pontos_1, pontos_2)

                                    # Atualiza o texto da pontuação na tela
                                    texto_pontuacao1, texto_pontuacao2 = atualizar_pontuacao(pontos_1, pontos_2, fonte_pontuacao, jogador1, jogador2)

                                    tabuleiro = [[0, 0, 0, 0],
                                                 [0, 0, 0, 0],
                                                 [0, 0, 0, 0]]
                                    jogador_atual = 1
                                    # Atualiza o texto da pontuação
                                    screen.blit(fundo, (0, 0))
                                    screen.blit(texto_pontuacao1, (width - largura_texto_pontuacao1 - 10, 10))
                                    screen.blit(texto_pontuacao2, (width - largura_texto_pontuacao2 - 10, 10 + altura_texto_pontuacao + 5))
                                    pygame.display.flip()

                                    time.sleep(0.5)   # Adicionar um atraso de 0.5 segundo aqui
                                    
                                    desenhar_tabuleiro(tabuleiro, largura_celula, screen, fundo, posicao_tabuleiro, width, altura_texto_pontuacao, altura_texto_jogador, largura_texto_pontuacao1, largura_texto_pontuacao2, largura_texto_jogador1, largura_texto_jogador2, texto_pontuacao1, texto_pontuacao2, texto_jogador1, texto_jogador2, altura_tabuleiro, largura_tabuleiro)

                                    continue

                                jogador_atual = alternar_jogador(jogador_atual)
                # Verifica se o botão Menu foi clicado
                if botao_menu.collidepoint(event.pos):
                    rodando = False
                    menu(width, height, title)
                    

        pygame.draw.rect(screen, (0, 0, 0), botao_menu)
        screen.blit(texto_menu, (botao_menu.centerx - texto_menu.get_width() // 2, botao_menu.centery - texto_menu.get_height() // 2))
        pygame.display.flip()

    pygame.quit()

def bot_dificil(tabuleiro):
   
    movimento_encontrado = False

    while not movimento_encontrado:
        for l in range(3):
            for i in range(4):
                if i < 2 and tabuleiro[l][i] == tabuleiro[l][i+1] != 0 and tabuleiro[l][i] == tabuleiro[l][+1] == tabuleiro[l][i+2] + 1 and 0 <= i+2 < 4:
                    fazer_jogada(tabuleiro, l, i+2)
                    movimento_encontrado = True
                    break
                if i < 2 and tabuleiro[l][i] == tabuleiro[l][i+2] != 0 and tabuleiro[l][i] == tabuleiro[l][i+2] == tabuleiro[l][i+1] + 1:
                    fazer_jogada(tabuleiro, l, i+1)
                    movimento_encontrado = True
                    break
                if 2 <= i <= 3 and tabuleiro[l][i] == tabuleiro[l][i-1] != 0 and tabuleiro[l][i] == tabuleiro[l][i-1] == tabuleiro[l][i-2] + 1:
                    fazer_jogada(tabuleiro, l, i-2)
                    movimento_encontrado = True
                    break
                if 2 <= i <= 3 and tabuleiro[l][i] == tabuleiro[l][i-2] != 0 and tabuleiro[l][i] == tabuleiro[l][i-2] == tabuleiro[l][i-1] + 1:
                    fazer_jogada(tabuleiro, l, i-1)
                    movimento_encontrado = True
                    break
            if movimento_encontrado:
                break
        
        if not movimento_encontrado:
            for c in range(4):
                if tabuleiro[0][c] == tabuleiro [1][c] != 0 and tabuleiro[0][c] == tabuleiro [1][c] == tabuleiro[2][c] + 1:
                    fazer_jogada(tabuleiro, 2, c)
                    movimento_encontrado = True
                    break
                if tabuleiro[0][c] == tabuleiro [2][c] != 0 and tabuleiro[0][c] == tabuleiro [2][c] == tabuleiro[1][c] + 1:
                    fazer_jogada(tabuleiro, 1, c)
                    movimento_encontrado = True
                    break
                if tabuleiro[2][c] == tabuleiro [1][c] != 0 and tabuleiro[2][c] == tabuleiro [1][c] == tabuleiro[0][c] + 1:
                    fazer_jogada(tabuleiro, 0, c)
                    movimento_encontrado = True
                    break
            if movimento_encontrado:
                break

        if not movimento_encontrado:
            for c in range(4):
                if 0 <= c <= 1 and tabuleiro[0][c] == tabuleiro[1][c+1] != 0 and tabuleiro[0][c] == tabuleiro[1][c+1] == tabuleiro[2][c+2] + 1:
                    fazer_jogada(tabuleiro, 2, c+2)
                    movimento_encontrado = True
                    break
                if 0 <= c <= 1 and tabuleiro[0][c] == tabuleiro[2][c+2] != 0 and tabuleiro[0][c] == tabuleiro[2][c+2] == tabuleiro[1][c+1] + 1:
                    fazer_jogada(tabuleiro, 1, c+1)
                    movimento_encontrado = True
                    break
                if 0 <= c <= 1 and tabuleiro[1][c+1] == tabuleiro[2][c+2] != 0 and tabuleiro[1][c+1] == tabuleiro[2][c+2] == tabuleiro[0][c] + 1:
                    fazer_jogada(tabuleiro, 0, c)
                    movimento_encontrado = True
                    break
                if 2 <= c <= 3 and tabuleiro[0][c] == tabuleiro[1][c-1] != 0 and tabuleiro[0][c] == tabuleiro[1][c-1] == tabuleiro[2][c-2] + 1:
                    fazer_jogada(tabuleiro, 2, c-2)
                    movimento_encontrado = True
                    break
                if 2 <= c <= 3 and tabuleiro[0][c] == tabuleiro[2][c-2] != 0 and tabuleiro[0][c] == tabuleiro[2][c-2] == tabuleiro[1][c-1] + 1:
                    fazer_jogada(tabuleiro, 1, c-1)
                    movimento_encontrado = True
                    break
                if 2 <= c <= 3 and tabuleiro[1][c-1] == tabuleiro[2][c-2] != 0 and tabuleiro[1][c-1] == tabuleiro[2][c-2] == tabuleiro[0][c] + 1:
                    fazer_jogada(tabuleiro, 0, c)
                    movimento_encontrado = True
                    break
            if movimento_encontrado:
                break
        
        if not movimento_encontrado:
            for l in range(3):
                if tabuleiro[l][0] != 0 and tabuleiro[l][3] != 3:
                    fazer_jogada(tabuleiro, random.randint(0, 2), 3)
                    movimento_encontrado = True
                    break
                if tabuleiro[l][3] != 0 and tabuleiro[l][0] != 3:
                    fazer_jogada(tabuleiro, random.randint(0, 2), 0)
                    movimento_encontrado = True
                    break
        
        if not movimento_encontrado:
            for c in range(4):
                for l in range(3):
                    if 0 < c < 3 and tabuleiro[0][c] != 0 and (tabuleiro[2][c+1] != 3 or tabuleiro[2][c-1] != 3):
                        if tabuleiro[2][c+1] == 3:
                            fazer_jogada(tabuleiro, 2, c-1)
                            movimento_encontrado = True
                            break
                        elif tabuleiro[2][c-1] == 3:
                            fazer_jogada(tabuleiro, 2, c+1)
                            movimento_encontrado = True
                            break
                        else:
                            if escolha() == 0:
                                fazer_jogada(tabuleiro, 2, c+1)
                                movimento_encontrado = True
                                break
                            elif escolha() == 1:
                                fazer_jogada(tabuleiro, 2, c-1)
                                movimento_encontrado = True
                                break
                    if 0 < c < 3 and tabuleiro[2][c] != 0 and (tabuleiro[0][c+1] != 3 or tabuleiro[0][c-1] != 3):
                        if tabuleiro[0][c+1] == 3:
                            fazer_jogada(tabuleiro, 0, c-1)
                            movimento_encontrado = True
                            break
                        elif tabuleiro[0][c-1] == 3:
                            fazer_jogada(tabuleiro, 0, c+1)
                            movimento_encontrado = True
                            break
                        else:    
                            if escolha() == 0:
                                fazer_jogada(tabuleiro, 0, c+1)
                                movimento_encontrado = True
                                break
                            elif escolha() == 1:
                                fazer_jogada(tabuleiro, 0, c-1)
                                movimento_encontrado = True
                                break
                    if tabuleiro[1][1] != 0 and (tabuleiro[0][3] != 3 or tabuleiro[2][3] != 3):
                        if tabuleiro[0][3] == 3:
                            fazer_jogada(tabuleiro, 2, 3)
                            movimento_encontrado = True
                            break
                        elif tabuleiro[2][3] == 3:
                            fazer_jogada(tabuleiro, 0, 3)
                            movimento_encontrado = True
                            break
                        else:   
                            if escolha() == 0:
                                fazer_jogada(tabuleiro, 0, 3)
                                movimento_encontrado = True
                                break
                            elif escolha() == 1:
                                fazer_jogada(tabuleiro, 2, 3)
                                movimento_encontrado = True
                                break
                    if tabuleiro[1][2] != 0 and (tabuleiro[0][0] != 3 or tabuleiro[2][0] != 3):
                        if tabuleiro[0][0] == 3:
                            fazer_jogada(tabuleiro, 2, 0)
                            movimento_encontrado = True
                            break
                        elif tabuleiro[2][0] == 3:
                            fazer_jogada(tabuleiro, 0, 0)
                            movimento_encontrado = True
                            break
                        else:    
                            if escolha() == 0:
                                fazer_jogada(tabuleiro, 0, 0)
                                movimento_encontrado = True
                                break
                            elif escolha() == 1:
                                fazer_jogada(tabuleiro, 2, 0)
                                movimento_encontrado = True
                                break
                
                if movimento_encontrado:
                    break
    
        if not movimento_encontrado:
            linha = random.randint(0, 2)
            coluna = random.randint(0, 3)
            while tabuleiro[linha][coluna] == 3:
                linha = random.randint(0, 2)
                coluna = random.randint(0, 3)

            fazer_jogada(tabuleiro, linha, coluna)
            movimento_encontrado = True
        
        return movimento_encontrado
    
    return tabuleiro

def regras(width, height, screen):
    pygame.init()

    fundo = pygame.image.load('imagem/bg1.png').convert_alpha()
    fundo = pygame.transform.scale(fundo, (width, height))
    rodando = True

    # Carregar fonte para os botões
    fonte_botoes = pygame.font.Font(None, 35)

    # Definir área dos botões
    botao_menu = pygame.Rect(width // 2 - -411, 643, 150, 50)
    texto_menu = fonte_botoes.render("Menu", True, (255, 255, 255))

    # Definir fonte do texto das regras
    fonte_regras = pygame.font.Font(None, 20)

    # Definir as regras do jogo
    regras_texto = [
        "O jogo do semáforo foi criado pelo matemático inglês Alan Parr, em 1998.",
        "O jogo tem o nome original de Traffic Lights.",
        "Segue a lógica do semáforo que vai do verde ao amarelo e deste para o vermelho.",
        "Este jogo joga-se com um tabuleiro retangular 3x4.",
        "São 24 peças disponíveis para ambos os jogadores, com 3 cores: 8 de cada cor sendo estas verde,",
        "amarelo e vermelho.",
        "Para ganhar é preciso o jogador ser o primeiro a formar uma linha de 3 peças da mesma cor",
        "na horizontal, na vertical ou na diagonal.",
        "",
        "Regras do jogo:",
        "- Escolhido quem será o primeiro, o jogo começa com a colocação de peças verdes em espaços vazios",
        "  de forma alternada pelos 2 jogadores.",
        "- As peças amarelas entram no jogo para substituir peças verdes quando estas já estiverem",
        "  posicionadas, as peças vermelhas devem apenas substituir as peças amarelas já colocadas",
        "  no lugar das verdes.",
        "- Nenhuma peça amarela ou vermelha pode ser colocada em espaços vazios. E uma peça verde não",
        "  pode substituir as demais depois de posicionadas.",
        "- Peça verde ou amarela pode ser substituída, mas após uma peça vermelha ser colocada no lugar",
        "  da amarela, não pode mais ser trocada, permanecendo fixa até ao final do jogo.",
        "- O jogador que conseguir formar uma fileira de 3 peças da mesma cor na horizontal, vertical",
        "  ou diagonal é o vencedor da partida."
    ]

    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if botao_menu.collidepoint(event.pos):
                    rodando = False
                    menu(width, height, title)

        screen.blit(fundo, (0, 0))

        # Desenhar regras na tela
        y = 40  # Posição vertical inicial para exibir as regras
        for linha in regras_texto:
            texto_regra = fonte_regras.render(linha, True, (255, 255, 255))
            screen.blit(texto_regra, (25, y))
            y += 25

        # Desenhar botões na tela
        pygame.draw.rect(screen, (0, 0, 0), botao_menu)
        screen.blit(texto_menu, (botao_menu.centerx - texto_menu.get_width() // 2, botao_menu.centery - texto_menu.get_height() // 2))

        pygame.display.update()

width = 1200
height = 720
pontos_1 = 0
pontos_2 = 0
title = "Jogo do Semáforo"
menu(width, height, title)
