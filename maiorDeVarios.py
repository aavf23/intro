def main():
    maior = -1

    print('O maior é:', pede_numero(maior))


def pede_numero(maior):
    while True:
        num = int(input('Qual o número? '))
        if num < 0:
            break
        else:
            valida_maior(maior, num)
    return maior


def valida_maior(maior, num):
    if num > maior:
        maior = num
    return maior


main()
