print('-------------------------')
print('|     JOGO DO GALO      |')
print('-------------------------')
print()
print('        1|2|3    ')
print('        -----')
print('        4|5|6    ')
print('        -----')
print('        7|8|9    ')

player_pos = []


def jogada(p):
    aux = 0
    for x in range(1, 6):
        if x % 2 == 0:
            print('-----')
        else:
            for y in range(1,6):
                for z in range(aux,aux+3):
                    if y % 2 == 1:
                        print('|', end='')
                    else:
                        if p == y:
                            print('X', end='')
                        else:
                            print(' ', end='')
                aux += 3


player_pos.append(int(input('Escolha a casa em que quer jogar: ')))

jogada(player_pos)
