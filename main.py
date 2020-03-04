import calculate

def main():
    checka = True
    while checka:
        n = int(input('Quandas casas decimais voce quer do pi?\n'))
        print(calculate.get_pi(n))
        test = input('Quer continuar: [s] [n]\n')
        if test == 's': 
            pass
        elif test == 'n':
            checka = False
        else:
            checka = False
    print("Obrigador por testar")

main()
