
# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# a. até 20 litros, desconto de 3% por litro
# b. acima de 20 litros, desconto de 5% por litro
# Gasolina:
# c. até 20 litros, desconto de 4% por litro
# d. acima de 20 litros, desconto de 6% por litro 

# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

tipocomb = input("Tipo de combustível (A)álcool ou (G)gasolina: ")
litrosvend = float(input("Quantidade de litros vendidos: "))

if tipocomb == 'A' or  tipocomb == 'a':
    precoal = litrosvend * 1.9
    print("Total a pagar em R$ %.2f " %precoal)

elif tipocomb == 'G' or tipocomb == 'g':
    precoga = litrosvend * 2.5
    print("Total a pagar em R$ %.2f " %precoga)

else:
    print("Valor incorreto para o tipo de combustível.")