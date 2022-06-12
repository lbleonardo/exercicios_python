
# Faça um Programa que leia três números e mostre o maior deles.

num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))
num3 = float(input("Insira o terceiro número: "))

if (num1 > num2) and (num2 > num3):
    print("O maior número é o primeiro: %.2f" %num1)
elif (num2 > num1) and (num2 > num3):
    print("O maior número é o segundo: %.2f" %num2)
elif (num3 > num1) and (num3 > num2):
    print("O maior número é o terceiro: %.2f" %num3)
elif (num1 == num2) and (num1 > num3):
    print("Os maiores números são o primeiro e o segundo: %.2f" %num1)
elif (num2 == num3) and (num2 > num1):
    print("Os maiores números são o segundo e o terceiro: %.2f" %num2)
elif (num1 == num3) and (num1 > num2):
    print("Os maiores números são o primeiro e o terceiro: %.2f" %num3)
else:
    print("Todos os números são iguais.")



