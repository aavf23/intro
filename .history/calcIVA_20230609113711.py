def main():

    prod = float(input("Introduze o preço do produto: "))
    cIVA(prod)
    print(prod)

def cIVA(p):
    p += p * 0.23
    return (p)

main()