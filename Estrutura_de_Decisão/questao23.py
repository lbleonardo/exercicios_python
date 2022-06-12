
# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

num = float(input("Informe um número: "))

if (int(num) == num):
    print("É um número inteiro.")
else:
    print("É um número decimal.")