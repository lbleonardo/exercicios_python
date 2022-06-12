# Exercício Estrutura Sequencial

# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# a) Para homens: (72.7*h) - 58
# b) Para mulheres: (62.1*h) - 44.7

sexo = input("Informe o seu sexo, M para masculino e F para meninino: ")

altura = float(input("Informe a sua altura em metros: "))

if sexo == "M" or sexo == "m":
    pIdealh = (72.7 * altura) - 58
    print("O seu peso ideal é: %.2f kg" %pIdealh)
elif sexo == "F" or sexo == "f":
    pIdealm = (62.1 * altura) - 44.7
    print("O seu peso ideal é: %.2f kg" %pIdealm)
else:
    print("Dados incorretos, tente novamente!")
    

