import random


print('-------------------------')
print('|     JOGO DO GALO      |')
print('-------------------------')
print()
print('        1|2|3    ')
print('        -----')
print('        4|5|6    ')
print('        -----')
print('        7|8|9    ')

player1 = {
    "name": 'human',
    'num': 0
}

player2 = {
    'name': 'cpu',
    'num': 0
}

board = ('1|2|3\n-----\n4|5|6\n-----\n7|8|9\n')

def jogada(p):

    global board
    aux = ''

    for i in range(len(board)-1):
        if board[i] != 'X' or board[i] != 'O':
            if p['name'] == 'human':
                aux = 'X'
            else:
                aux = 'O'
            break
    
    board = board.replace(str(p['num']), aux)
    print(board)

    # aux = 1
    # for x in range(4):
    #     if x % 2 == 1:
    #         print('-----')
    #     else:
    #         for y in range(5):
    #             for w in range(aux, aux+2):
    #                 for z in p:
    #                     if y % 2 == 1:
    #                         print('|', end='')
    #                     else:
    #                         if p == z:
    #                             print('X', end='')
    #                         else:
    #                             print(' ', end='')
    #                 aux += 3


while True:

    player1['num'] = int(input('Escolha a casa em que quer jogar: '))
    for i in range(len(board)-1):
        if board[i] == str(player1['num']):
            jogada(player1)
            break
        if i == len(board)-1:
            print('Escolha outro número!')
            continue

    player2['num']
    for i in range(len(board) - 1):
            if (board[i] == str(player2['num'])) and (player1['num'] != player2['num']):
                jogada(player2)
                break
