def main():

    prod = float(input("Introduze o preço do produto: "))
    prod = cIVA(prod)
    print(prod)

def cIVA(p):
    p += p * 0.23
    return (p)

main()