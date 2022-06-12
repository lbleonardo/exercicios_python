
# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

num = input("Informe um número menor que 1000: ")
tam = len(num)

if int(num) < 1000:
    if tam == 3:
        p1 = num[0]
        p2 = num[1]
        p3 = num[2]
        print(p1, "centena(s)", p2, "dezena(s) e", p3, "unidade(s).")

    elif tam == 2:
        p1 = num[0]
        p2 = num[1]    
        print(p1, "dezena(s) e", p2, "unidade(s).")

    elif tam == 1:
        p1 = num[0]
        print(p1, "unidade(s).")

else:
    print("Informe um valor abaixo de 1000.")    