
# Faça um Programa que peça dois números e imprima o maior deles.

num1 = int(input("Insira um número inteiro: "))
num2 = int(input("Insira um outro número inteiro: "))

if num1 > num2:
    print("O maior número é %.0f" %num1)
elif num1 == num2:
    print("O números são iguais.")
else:
    print("O maior número é %.0f" %num2)
