
# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

preco1 = float(input("Informe o preço do produto A: "))
preco2 = float(input("Informe o preço do produto B: "))
preco3 = float(input("Informe o preço do produto C: "))

if (preco1 > preco2) and (preco2 > preco3):
    print("Deve comprar o produto C que tem o preço de R$ %.2f" %preco3)
elif (preco1 < preco2) and (preco1 > preco3):
    print("Deve comprar o produto C que tem o preço de R$ %.2f" %preco3)
elif (preco2 > preco3) and (preco3 > preco1):
    print("Deve comprar o produto A que tem o preço de R$ %.2f" %preco1)
elif (preco2 < preco3) and (preco2 > preco1):
    print("Deve comprar o produto A que tem o preço de R$ %.2f" %preco1)
elif (preco3 > preco1) and (preco1 > preco2):
    print("Deve comprar o produto B que tem o preço de R$ %.2f" %preco2)
elif (preco3 < preco1) and (preco3 > preco2):
    print("Deve comprar o produto B que tem o preço de R$ %.2f" %preco2)
else:
    print("Todos os preços são iguais.")
