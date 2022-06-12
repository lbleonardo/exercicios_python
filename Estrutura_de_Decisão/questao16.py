
# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

a = int(input("Informe o valor de a: "))
b = int(input("Informe o valor de b: "))
c = int(input("Informe o valor de c: "))

delta = b**2 - 4*a*c



print("O valor de delta é:", delta)

if a == 0:
    print("Esta equação não é do segundo grau.")
elif delta == 0:
    x1 = (-b + (delta**0.5)) / (2*a)
    print("A equação possui apenas uma raiz real no valor de: %.2f" %x1)
elif delta > 0:
    x1 = (-b + (delta**0.5)) / (2*a)
    x2 = (-b - (delta**0.5)) / (2*a)
    print("A equação possui duas raízes reais nos valores de: %.2f e %.2f." %(x1, x2))
else:
    print("A equação não possui raízes reais.")



