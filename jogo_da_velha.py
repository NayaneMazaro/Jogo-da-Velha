from random import randrange

def display_board(board):
    print("+" + "-------+"*3)
    for linha in range(3):
        print("|" + "       |" * 3)
        for colunaunauna in range(3):
            print("|   " + str(board[linha][colunaunauna]) + "   ", end="")
        print("|")
        print("|" + "       |" * 3)
        print("+" + "-------+"*3)

def mov_jogador(board):
    verificado = False
    while not verificado:
        jogada = int(input("Qual a sua jogada?: "))
        if (jogada > 0 and jogada < 10):
            for i, linha in enumerate(board):
                if jogada in linha:
                    posicao = linha.index(jogada)
                    board[i][posicao] = 'O'  # marca a jogada no tabuleiro
                    return
            else:
                print("Jogada inválida - tente outra vez!\n")

def lista_campos_livres(board):
    campos_livres = [(linha, colunauna) for linha in range(3) for colunauna in range(3)
                     if board[linha][colunauna] not in ['O', 'X']]
    return campos_livres

def vitoria_para(board, sinal):
    if sinal == "X":
        quem = "Eu"
    elif sinal == "O":
        quem = "Você"
    else:
        quem = None
    diagonal1 = diagonal2 = True
    for lc in range(3):
        if board[lc][0] == sinal and board[lc][1] == sinal and board[lc][2] == sinal: # verifica a linha
            return quem
        if board[0][lc] == sinal and board[1][lc] == sinal and board[2][lc] == sinal: # verifica a colunauna
            return quem
        if board[lc][lc] != sinal: # verifica a primeira diagonal
            diagonal1 = False
        if board[2 - lc][2 - lc] != sinal: # verifica a segunda diagonal
            diagonal2 = False
    if diagonal1 or diagonal2:
        return quem
    return None


def mov_computador(board):
    livre = lista_campos_livres(board) # faz uma lista de campos livres
    cnt = len(livre)
    if cnt > 0:
        this = randrange(cnt)
        linha, coluna = livre[this]
        board[linha][coluna] = "X"

board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] 
board[1][1] = 'X' # primeiro 'X' no meio
livre = lista_campos_livres(board)
turno_jogador = True

while len(livre):
    display_board(board)
    if turno_jogador:
        mov_jogador(board)
        vitoria = vitoria_para(board, "O")
    else:
        mov_computador(board)
        vitoria = vitoria_para(board, "X")
    if vitoria != None:
        break
    turno_jogador = not turno_jogador
    livre = lista_campos_livres(board)
    
display_board(board)
if vitoria == "Você":
    print("Você ganhou!")
elif vitoria == "Eu":
    print("Você perdeu!")
else:
    print("Empate!")
