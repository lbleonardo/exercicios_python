# Exercício Estrutura Sequencial

# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

salHoras = float(input("Salário por hora: "))
horaMes = int(input("Horas trabalhadas por mês: "))

total = salHoras * horaMes

print("O seu salário no mês é $ %.2f" %total)