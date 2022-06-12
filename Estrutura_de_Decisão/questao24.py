
# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.

num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))
operacao = input("Operação entre os número (A)adição, (S)subtração, (M)multiplicação, (D)divisão: ")

if operacao == 'A' or operacao == 'a':
    soma = num1 + num2
    if soma > 0:
        if (int(soma) == soma):
            if soma % 2 == 0:
                print("%.0f é par, positivo e inteiro." %soma)
            else:
                print("%.0f é ímpar, positivo e inteiro." %soma)
        else:
            restodec = (soma - int(soma))
            decaprox = round(restodec,1)

            if (decaprox*10) % 2 == 0:
                print("%.2f é par, positivo e decimal." %soma)
            else:
                print("%.2f é ímpar, positivo e decimal." %soma)
    elif soma == 0:
        print("%.0f é um número neutro." %soma)
    else:
        if (int(soma) == soma):
            if soma % 2 == 0:
                print("%.0f é par, negativo e inteiro." %soma)        
            else:
                print("%.0f é ímpar, negativo e inteiro." %soma)
        
        else:
            restodec = (soma - int(soma))
            decaprox = round(restodec,1)

            if (decaprox*10) % 2 == 0:
                print("%.2f é par, negativo e decimal." %soma)
            else:
                print("%.2f é ímpar, negativo e decimal." %soma)

elif operacao == 'S' or operacao == 's':
    subtracao = num1 - num2

    if subtracao > 0:
        if (int(subtracao) == subtracao):
            if subtracao % 2 == 0:
                print("%.0f é par, positivo e inteiro." %subtracao)
            else:
                print("%.0f é ímpar, positivo e inteiro." %subtracao)
        else:
            restodec = (subtracao - int(subtracao))
            decaprox = round(restodec,1)

            if (decaprox*10) % 2 == 0:
                print("%.2f é par, positivo e decimal." %subtracao)
            else:
                print("%.2f é ímpar, positivo e decimal." %subtracao)
    
    elif subtracao == 0:
        print("%.0f é um número neutro." %subtracao)

    else:
        if (int(subtracao) == subtracao):
            if subtracao % 2 == 0:
                print("%.0f é par, negativo e inteiro." %subtracao)        
            else:
                print("%.0f é ímpar, negativo e inteiro." %subtracao)
        
        else:
            restodec = (subtracao - int(subtracao))
            decaprox = round(restodec,1)

            if (decaprox*10) % 2 == 0:
                print("%.2f é par, negativo e decimal." %subtracao)
            else:
                print("%.2f é ímpar, negativo e decimal." %subtracao)

elif operacao == 'M' or operacao == 'm':
    multiplicacao = num1 * num2

    if multiplicacao > 0:
        if (int(multiplicacao) == multiplicacao):
            if multiplicacao % 2 == 0:
                print("%.0f é par, positivo e inteiro." %multiplicacao)
            else:
                print("%.0f é ímpar, positivo e inteiro." %multiplicacao)
        else:
            restodec = (multiplicacao - int(multiplicacao))
            decaprox = round(restodec,2)

            if (decaprox*100) % 2 == 0:
                print("%.2f é par, positivo e decimal." %multiplicacao)
            else:
                print("%.2f é ímpar, positivo e decimal." %multiplicacao)
    
    elif multiplicacao == 0:
        print("%.0f é um número neutro." %multiplicacao)

    else:
        if (int(multiplicacao) == multiplicacao):
            if multiplicacao % 2 == 0:
                print("%.0f é par, negativo e inteiro." %multiplicacao)        
            else:
                print("%.0f é ímpar, negativo e inteiro." %multiplicacao)
        
        else:
            restodec = (multiplicacao - int(multiplicacao))
            decaprox = round(restodec,2)

            if (decaprox*100) % 2 == 0:
                print("%.2f é par, negativo e decimal." %multiplicacao)
            else:
                print("%.2f é ímpar, negativo e decimal." %multiplicacao)

elif operacao == 'D' or operacao == 'd':
    divisao = num1 / num2

    if divisao > 0:
        if (int(divisao) == divisao):
            if divisao % 2 == 0:
                print("%.0f é par, positivo e inteiro." %divisao)
            else:
                print("%.0f é ímpar, positivo e inteiro." %divisao)
        else:
            restodec = (divisao - int(divisao))
            decaprox = round(restodec,2)

            if (decaprox*100) % 2 == 0:
                print("%.2f é par, positivo e decimal." %divisao)
            else:
                print("%.2f é ímpar, positivo e decimal." %divisao)
    
    elif divisao == 0:
        print("%.0f é um número neutro." %divisao)

    else:
        if (int(divisao) == divisao):
            if divisao % 2 == 0:
                print("%.0f é par, negativo e inteiro." %divisao)        
            else:
                print("%.0f é ímpar, negativo e inteiro." %divisao)
        
        else:
            restodec = (divisao - int(divisao))
            decaprox = round(restodec,2)

            if (decaprox*100) % 2 == 0:
                print("%.2f é par, negativo e decimal." %divisao)
            else:
                print("%.2f é ímpar, negativo e decimal." %divisao)

else:
    print("Operação inválida!")