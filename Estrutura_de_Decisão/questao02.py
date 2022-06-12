
# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num1 = int(input("Insira um número inteiro: "))

if num1 > 0:
    print("Número %.0f é positivo" %num1)
elif num1 == 0:
    print("Zero é um número neutro.")
else:
    print("Número %.0f é negativo" %num1)
