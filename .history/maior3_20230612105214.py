
def main():

    num1, num2, num3 = range(int(input('Insira 3 numeros'))

    if (num1 > num2 and num1 > num3):
        maior = num1
    if (num2 > num1 and num2 > num3):
        maior = num2
    if num3 > num2 and num3 > num1:
        maior = num3

    print('O número maior é', maior)


main()
