# Exercício Estrutura Sequencial

# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

import math

ladoq = int(input("Informe o lado do quadrado: "))
areaq = ladoq ** 2
dobroa = areaq * 2

print("O dobro da área do quadrado é: %.0f" %dobroa)