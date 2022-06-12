# Exercício Estrutura Sequencial

# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

raio = float(input("Informe o raio do círculo: "))
PI = math.pi
area = PI * raio**2

print("A área do círculo é: %.2f" %area)
