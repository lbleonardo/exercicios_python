# Exercício Estrutura Sequencial


#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a) o produto do dobro do primeiro com metade do segundo.
# b) a soma do triplo do primeiro com o terceiro.
# c) o terceiro elevado ao cubo.

numA = int(input("Insira o primeiro número inteiro: "))
numB = int(input("Insira o segundo número inteiro: "))
numC = float(input("Insira um número real: "))

a = (2*numA) * (numB/2)
b = (3*numA) + numC
c = numC**3

print("O produto do dobro do primeiro com metade do segundo:", a)
print("A soma do triplo do primeiro com o terceiro:", b)
print("O terceiro elevado ao cubo: %.2f" %c)