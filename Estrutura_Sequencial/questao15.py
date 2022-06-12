# Exercício Estrutura Sequencial

# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

# a) salário bruto.
# b) quanto pagou ao INSS.
# c) quanto pagou ao sindicato.
# d) o salário líquido.
# e) calcule os descontos e o salário líquido, conforme a tabela abaixo:

# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

salHora = float(input("Informe quanto você ganha por hora trabalhada: "))
horaMes = int(input("Informe a quantidade de horas trabalhadas por mês: "))

salBruto = salHora * horaMes
iRenda = salBruto*0.11
inss = salBruto*0.08
sindicato = salBruto*0.05
salLiquido = salBruto - (iRenda + inss + sindicato)

print("Salário Bruto: R$ %.2f" %salBruto)
print("Imposto de Renda: R$ %.2f" %iRenda)
print("INSS: R$ %.2f" %inss)
print("Sindicato: R$ %.2f" %sindicato)
print("Salário Líquido: R$ %.2f" %salLiquido)


