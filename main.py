
# ' ': campo inválido
# 'o': campo com peça
# '_': campo vazio

tabuleiro = [
    [' ',' ','o','o','o',' ',' '],
    [' ',' ','o','o','o',' ',' '],
    ['o','o','o','o','o','o','o'],
    ['o','o','o','_','o','o','o'],
    ['o','o','o','o','o','o','o'],
    [' ',' ','o','o','o',' ',' '],
    [' ',' ','o','o','o',' ',' '],
]
conjunto_jogadas = set()
conjunto_tabuleiros = set()

COMPRIMENTO = 7

def imprime_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        campo_string = ''
        for campo in linha:
            campo_string = campo_string + campo + ' '
        print (campo_string)
    print ('_______________')

def imprime_jogadas(jogadas):
    print ('Jogadas:')
    for jogada in jogadas:
        x, y, direcao = jogada
        print (x+1, y+1, direcao)

def identificador_tabuleiro(tabuleiro):
    return ''.join([item for linha in tabuleiro for item in linha])

def identificador_jogada(x, y, direcao, tabuleiro):
    tabuleiro_string = identificador_tabuleiro(tabuleiro)
    return f'{x}.{y}.{direcao}.{tabuleiro_string}'

def campo_valido(x, y):
    if y < 0 or y > 6:
        return False
    if x < 0 or x > 6:
        return False
    if tabuleiro[x][y] == ' ':
        return False
    return True

def move(x, y, direcao):
    if campo_valido(x, y) == False:
        return False

    if tabuleiro[x][y] != 'o':
        print (f'Movimento inválido. Não é uma peça! {x},{y}')
        return False

    if direcao == 'cima':
        if x < 2:
            print (f'Posição x inválida: {x},{y}')
            return False

        if tabuleiro[x-2][y] == '_' and tabuleiro[x-1][y] == 'o':
            tabuleiro[x-2][y] = 'o'
            tabuleiro[x-1][y] = '_'
            tabuleiro[x][y] = '_'
            return True
        else:
            print (f'Movimento inválido: {x},{y}')
            return False

    elif direcao == 'baixo':
        if x > 4:
            print (f'Posição x inválida: {x},{y}')
            return False

        if tabuleiro[x+2][y] == '_' and tabuleiro[x+1][y] == 'o':
            tabuleiro[x+2][y] = 'o'
            tabuleiro[x+1][y] = '_'
            tabuleiro[x][y] = '_'
            return True
        else:
            print ('Movimento inválido!')
            return False
    elif direcao == 'esquerda':
        if y < 2:
            print (f'Posição y inválida: {x},{y}')
            return False

        if tabuleiro[x][y-2] == '_' and tabuleiro[x][y-1] == 'o':
            tabuleiro[x][y-2] = 'o'
            tabuleiro[x][y-1] = '_'
            tabuleiro[x][y] = '_'
            return True
        else:
            print (f'Movimento inválido: {x},{y}')
            return False
    elif direcao == 'direita':
        if y > 4:
            print (f'Posição y inválida: {x},{y}')
            return False

        if tabuleiro[x][y+2] == '_' and tabuleiro[x][y+1] == 'o':
            tabuleiro[x][y+2] = 'o'
            tabuleiro[x][y+1] = '_'
            tabuleiro[x][y] = '_'
            return True
        else:
            print (f'Movimento inválido: {x},{y}')
            return False
    else:
        print ('Direção inválida!')
        return False


def verifica_fim_jogo():
    encontrou_peca = False
    for linha in tabuleiro:
        for campo in linha:
            if campo == 'o':
                if encontrou_peca == True:
                    return False
                else:
                    encontrou_peca = True
    return encontrou_peca

def le_comando():
    comando = input("Jogada (ex: linha,coluna,direção): ")
    if ',' not in comando:
        return None

    x, y, direcao = comando.split(',')
    x = int(x)
    y = int(y)
    return x, y, direcao

def inicia_jogo():
    while True:
        imprime_tabuleiro(tabuleiro)

        comando = le_comando()
        if comando is None:
            print ('Comando inválido. Tente novamente...')
            continue

        x, y, direcao = comando
        move(x, y, direcao)

        if verifica_fim_jogo() == True:
            print ('Parabens você ganhou o jogo!')
            break

def pega_jogadas_validas(x, y):
    jogadas_validas = []
    if campo_valido(x-2, y) and campo_valido(x-1, y) and tabuleiro[x-2][y] == 'o' and tabuleiro[x-1][y] == 'o':
        jogadas_validas.append((x-2, y, 'baixo'))
    if campo_valido(x+2, y) and campo_valido(x+1, y) and tabuleiro[x+2][y] == 'o' and tabuleiro[x+1][y] == 'o':
        jogadas_validas.append((x+2, y, 'cima'))
    if campo_valido(x, y-2) and campo_valido(x, y-1) and tabuleiro[x][y-2] == 'o' and tabuleiro[x][y-1] == 'o':
        jogadas_validas.append((x, y-2, 'direita'))
    if campo_valido(x, y+2) and campo_valido(x, y+1) and tabuleiro[x][y+2] == 'o' and tabuleiro[x][y+1] == 'o':
        jogadas_validas.append((x, y+2, 'esquerda'))
    return jogadas_validas

def decide_movimento(tabuleiro):
    for i in range(COMPRIMENTO):
        for j in range(COMPRIMENTO):
            if tabuleiro[i][j] == '_':
                jogadas = pega_jogadas_validas(i, j)
                for jogada in jogadas:
                    x, y, direcao = jogada
                    jogada_id = identificador_jogada(x, y, direcao, tabuleiro)
                    if jogada_id not in conjunto_jogadas:
                        return jogada
    return None

def desfaz_jogada(x, y, direcao):
    tabuleiro[x][y] = 'o'
    if direcao == 'baixo':
        tabuleiro[x+1][y] = 'o'
        tabuleiro[x+2][y] = '_'
    elif direcao == 'cima':
        tabuleiro[x-1][y] = 'o'
        tabuleiro[x-2][y] = '_'
    elif direcao == 'direita':
        tabuleiro[x][y+1] = 'o'
        tabuleiro[x][y+2] = '_'
    elif direcao == 'esquerda':
        tabuleiro[x][y-1] = 'o'
        tabuleiro[x][y-2] = '_'

def espelha_coluna(tabuleiro):
    tabuleiro_espelhado_colunas = []
    for linha in tabuleiro:
        nova_linha = []
        for item in linha:
            nova_linha.insert(0, item)
        tabuleiro_espelhado_colunas.append(nova_linha)
    return tabuleiro_espelhado_colunas

def espelha_linha(tabuleiro):
    return tabuleiro[::-1]

def pega_espelhamentos(tabuleiro):
    semelhantes = []
    novo = espelha_coluna(tabuleiro)
    semelhantes.append(novo)
    novo = espelha_linha(novo)
    semelhantes.append(novo)
    novo = espelha_linha(tabuleiro)
    semelhantes.append(novo)
    return semelhantes

def gira_tabuleiro(tabuleiro):
    novo_tabuleiro = [[' ' for _ in range(COMPRIMENTO)] for _ in range(COMPRIMENTO)]
    for linha in range(COMPRIMENTO):
        for coluna in range(COMPRIMENTO):
            novo_tabuleiro[coluna][COMPRIMENTO-1-linha] = tabuleiro[linha][coluna]
    return novo_tabuleiro


def pega_tabuleiros_semelhantes(tabuleiro):
    semelhantes = []
    espelhamentos = pega_espelhamentos(tabuleiro)
    semelhantes.extend(espelhamentos)
    girado = gira_tabuleiro(tabuleiro)
    semelhantes.append(girado)
    espelhamentos_girados = pega_espelhamentos(girado)
    semelhantes.extend(espelhamentos_girados)
    return semelhantes


def resolve_jogo():
    turno = 1
    nivel = 1
    max_nivel = 1

    jogadas = []

    while True:
        if nivel >= max_nivel:
            max_nivel = nivel
            print (f'Turno {turno} | Nivel {nivel} | Max Nivel {max_nivel}')
            imprime_tabuleiro(tabuleiro)

        movimento = decide_movimento(tabuleiro)
        if movimento is None:
            ultima_jogada = jogadas.pop()
            x, y, direcao = ultima_jogada
            nivel -= 1
            desfaz_jogada(x, y, direcao)
            continue

        # print (f'Movimento: {movimento}')
        jogadas.append(movimento)

        x, y, direcao = movimento
        jogada_id = identificador_jogada(x, y, direcao, tabuleiro)
        conjunto_jogadas.add(jogada_id)

        move(x, y, direcao)

        tabuleiro_id = identificador_tabuleiro(tabuleiro)

        if tabuleiro_id in conjunto_tabuleiros:
            ultima_jogada = jogadas.pop()
            x, y, direcao = ultima_jogada
            desfaz_jogada(x, y, direcao)
            continue

        # adiciona o proprio tabuleiro
        conjunto_tabuleiros.add(tabuleiro_id)
        # adiciona os tabuleiros semelhantes
        tabuleiros_semelhantes = pega_tabuleiros_semelhantes(tabuleiro)
        for t in tabuleiros_semelhantes:
            tabuleiro_id = identificador_tabuleiro(t)
            conjunto_tabuleiros.add(tabuleiro_id)

        turno += 1
        nivel += 1

        if verifica_fim_jogo() == True:
            print (f'Turno {turno} | Nivel {nivel} | Max Nivel {max_nivel}')
            imprime_tabuleiro(tabuleiro)
            imprime_jogadas(jogadas)
            print ('Parabens você ganhou o jogo!')
            break

        if turno == 1000000:
            break


if __name__ == '__main__':
    print ("Começando o jogo...")

    # inicia_jogo()
    resolve_jogo()