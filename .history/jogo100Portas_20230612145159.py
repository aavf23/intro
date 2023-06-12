import random


def main():

    porta = random.randint(1, 100)
    num = int(input('Adivinhe o número da porta entre 1 e 100: '))

    while num < 1 or num > 100:
        num = int(input('Tem de escolher um número entre 1 e 100!! '))
    
    jogada(num, porta)

def jogada(num, porta):
    
    tentativas = 4
    resultado = ''
    
    while True:
        if tentativas == 0:
            resultado print('Perdeu o jogo!!')
            break
        elif num != porta:
            print('Tem', tentativas, 'tentativa/s!!')
            tentativas -= 1

        if num == porta:
            print('Ganhou o jogo!!')
            break
        elif num > porta:
            print('Mais baixo!')
        else:
            print('Mais alto!!')
    
    return resultado


main()
