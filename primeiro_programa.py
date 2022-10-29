from random import randrange

def display_board(board):
    print("+-------" * 3,"+", sep="")
    for row in range(3):
        print("|       " * 3,"|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3,"|",sep="")
        print("+-------" * 3,"+",sep="")

def enter_move(board):
    ok = False #utilizada para entrar no loop
    while not ok:
        move = input("Entre com seu movimento: ")
        ok = len(move) == 1 and move >= '1' and move <= '9' #entrada válida?
        if not ok:
            print("Movimento ruim - Faça outro!") #entrada não válidada
            continue
        move = int(move) -1 #celúla de 0 a 8
        row = move // 3 #linha
        col = move % 3 #coluna
        sign = board[row][col] #check no espço escolhido
        ok = sign not in ['O', 'X'] 
        if not ok: #caso o espaço já esteja ocupado
            print("Espaço ocupado, tente outro.")
            continue
    board[row][col] = 'O' ## define '0' no quadrado selecionado

def make_list_of_free_fields(board):
    free = [] # a lista está vazia inicialmente
    for row in range(3): # iterar pelas linhas
        for col in range(3): #iterar pelas colunas
            if board[row][col] not in ['O', 'X']: #célula livre?
                free.append((row,col)) #sim, é - anexar nova tupla à lista
        return free


def victory_for(board, sgn):
    if sgn == "X": #estamos procurando X?
        who = 'me' #sim - é do lado do computador
    elif sgn == "O": #... ou para O?
        who = 'you' #sim, nossa vez
    else:
        who = None #não devemos cair aqui!
    cross1 = cross2 = True #para diagonais
    for rc in range(3):
        if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn: #check linha rc
            return who
        if board[0][rc] == sgn and board[1][rc] == sgn and board [2][rc] == sgn: #check coluna
            return who
        if board[rc][rc] != sgn: #check primeira diagonal
            cross1 = False
        if board[2 - rc][2 - rc] != sgn: #check a segunda diagonall
            cross2 = False
    if cross1 or cross2:
        return who
    return None

def draw_move(board):
    free = make_list_of_free_fields(board) #faz uma lista de campos livres
    cnt = len(free)
    if cnt > 0: #se a lista não estiver vazia, escolha um lugar para 'X' e defina-o
        this = randrange(cnt)
        row, col = free[this]
        board[row][col] = 'X'

board = [ [3 * j + i + 1 for i in range(3)] for j in range(3)] #fazer um tabuleiro vazio
board [1][1] = 'X' #marquue o primeiro 'X' no meio
free = make_list_of_free_fields(board)
human_turn = True #que turno é agora?
while len(free):
    display_board(board)
    if human_turn:
        enter_move(board)
        victor = victory_for(board,'0')
    else:
        draw_move(board)
        victor = victory_for(board,'X')
    if victor != None:
        break
    human_turn = not human_turn
    free = make_list_of_free_fields(board)


display_board(board)
if victor == 'you':
    print("Você venceu!")
elif victor == 'me':
    print("Eu venci")
else:
    print("Velha!")
