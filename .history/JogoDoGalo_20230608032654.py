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

while True:

    
    player_pos.append(int(input('Escolha a casa em que quer jogar: ')))

    jogada(player_pos)
    jogada(cpu)
