import random


def main():

    porta = random.randint(1, 100)
    print(porta)
    tentativas = 0
    resultado = ''

    while True:

        if tentativas > 10:
            resultado = 'A casa de banho fica na porta Nº ' + \
                str(porta) + '!!\nErrou na porta e molhou-se, que embaraçoso!!'
            break

        num = int(input('Adivinhe o número da porta entre 1 e 100: '))

        while num < 1 or num > 100:
            num = int(input('Tem de escolher um número entre 1 e 100!! '))

        if num == porta:
            resultado = 'Acertou no número!! '
            if (tentativas < 3):
                resultado += 'Boa pontaria!!'
            elif tentativas < 5:
                resultado += 'Não precisava de vir a correr!!'
            elif tentativas < 8:
                resultado += 'Ainda conseguia aguentar mais um pouco!!'
            elif tentativas <= 10:
                resultado += 'Esteve perto dum acidente!!'
            break
        elif num > porta:
            print('Mais baixo!')
        else:
            print('Mais alto!!')

        if num != porta or tentativas < 10:
            
            print('Vai na', tentativas, 'ª tentativa!!')
            tentativas += 1

    print(resultado)


main()
