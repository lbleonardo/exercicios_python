
# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

dia = int(input("Informe o dia: "))
mes = int(input("Informe o mês: "))
ano = int(input("Informe o ano: "))

if mes == 1 or mes == 3 or mes== 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dia >= 1 and dia <= 31:
        print("Data Válida")
    else:
        print("Data Inválida")

elif mes == 2:
    if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
        if dia >= 1 and dia <= 29:
            print("Data Válida")
        else:                        
            print("Data Inválida")   
    else:
        if dia >= 1 and dia <= 28:
            print("Data Válida")
        else:
            print("Data Inválida")
    
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia >= 1 and dia <= 30:
        print("Data Válida")
    else:
        print("Data Inválida")

else:
    print("Data Inválida")
