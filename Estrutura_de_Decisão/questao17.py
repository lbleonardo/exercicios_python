
# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

ano = int(input("Informe um ano: "))

if (ano % 4 == 0):
    if (ano % 100 == 0):
        if (ano % 400 == 0):
            print("É bissexto!")
        else:
            print("Não é bissexto!")
    else:
        print("É bissexto!")
else:
    print("Não é bissexto!")

