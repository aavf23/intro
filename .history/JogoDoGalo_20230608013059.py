print('-------------------------')
print('|     JOGO DO GALO      |')
print('-------------------------')
print()
print('        1|2|3    ')
print('        -----')
print('        4|5|6    ')
print('        -----')
print('         | |     ')


player_pos = input('Escolha a casa em que quer jogar: ')

def jogada():
    for x in range(player_pos[0]):
        for y in range(player_pos[1]):

