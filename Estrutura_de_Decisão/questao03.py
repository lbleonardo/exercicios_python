
# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo=input("Informe o seu sexo F para Feminino e M para Masculino: ")

if (sexo == "F") or (sexo == "f"):
    print("Feminino.")
elif (sexo == "M") or (sexo == "m"):
    print("Masculino.")
else:
    print("Sexo Inválido.")
