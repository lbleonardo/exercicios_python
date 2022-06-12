
# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

print("PROGRAMA DE UM CAIXA ELETRÔNICO")
print("Cédulas DISPONÍVEIS: 1, 5, 10, 50 e 100")

saque=int(input("Informe o valor do saque em reais, mínimo de 10 e máximo de 600: "))

if (saque >= 10) and (saque < 100):
    saque = str(saque)
    pos1 = int(saque[0])
    pos2 = int(saque[1])

    if pos1 >= 1 and pos1 < 5:
        if pos2 > 0 and pos2 < 5:
            print("%.0f nota(s) de dez e %.0f nota(s) de 1." %(pos1,pos2))
        elif pos2 == 0:
            print("%.0f notas(s) de dez." %pos1)
        else:
            print("%.0f nota(s) de dez, 1 nota de cinco e %.0f nota(s) de 1." %(pos1,pos2-5))
    
    elif pos1 >= 5 and pos1 <= 9:
        nota50 = pos1 // 5
        nota10 = pos1 % 5
        if pos1 == 5 and pos2 == 0:
            print("%.0f nota de cinquenta" %nota50)
        elif pos1 == 5 and pos2 < 5:
            print("%.0f nota de cinquenta e %.0f nota(s) de 1." %(nota50,pos2))
        elif pos1 == 5 and pos2 == 5:
            print("%.0f nota de cinquenta e %.0f nota de 5." %(nota50,pos2/5))
        elif pos1 == 5 and pos2 > 5:
            print("%.0f nota de cinquenta, 1 nota de 5 e %.0f nota(s) de 1." %(nota50,pos2-5))
        elif pos2 > 0 and pos2 < 5:
            if pos1 > 5:
                print("%.0f nota(s) de cinquenta, %.0f nota(s) de 10 e %.0f nota(s) de 1." %(nota50,nota10,pos2))
            elif pos1 == 5:
                print("%.0f nota de cinquenta e %.0f nota de 1." %(nota50,pos2))        
        elif pos2 == 0:
            print("%.0f notas(s) de cinquenta e %.0f nota(s) de dez." %(nota50,nota10))
        else:
            print("%.0f nota(s) de cinquenta, %.0f nota(s) de 10, 1 nota de 5 e %.0f nota(s) de 1." %(nota50,nota10,pos2-5))

elif (saque >= 100) and (saque <= 600):    
    saque = str(saque)
    pos1 = int(saque[0])
    pos2 = int(saque[1])
    pos3 = int(saque[2])
    nota100 = int(saque) // 100   
    
    if (pos1 > 0) and (pos1 <= 5):
        nota50 = pos2 // 5
        nota10 = pos2 % 5
        nota5 = pos3 // 5
        nota1 = pos3 % 5

        if (pos2 >= 0) and (pos2 <= 9) and (pos3 >= 0) and (pos3 <= 9):
            if (pos2 == 0):
                if (pos3 == 0):
                    print("%.0f nota(s) de 100." %(nota100))

                elif (pos3 > 0) and (pos3 < 5):
                    print("%.0f nota(s) de 100 e %.0f nota(s) 1." %(nota100,nota1))

                elif (pos3 == 5):
                    print("%.0f nota(s) de 100 e %.0f nota(s) de 5." %(nota100,nota5))
                
                else:
                    print("%.0f nota(s) de 100 e %.0f nota(s) de 5 e %.0f nota(s) de 1." %(nota100,nota5,nota1))

            elif (pos3 == 0):
                if (pos2 > 0) and (pos2 < 5):
                    print("%.0f nota(s) de 100 e %.0f nota(s) de 10." %(nota100,nota10))
                
                elif (pos2 == 5):
                    print("%.0f nota(s) de 100 e %.0f nota(s) de 50." %(nota100,nota50))

                else:
                    print("%.0f nota(s) de 100 e %.0f nota(s) de 50 e %.0f nota(s) de 10." %(nota100,nota50,nota10))

            elif (pos2 > 0) and (pos2 < 5):
                if (pos3 > 0) and (pos3 < 5):
                    print("%.0f nota(s) de 100, %.0f nota(s) de 10 e %.0f nota(s) de 1." %(nota100,nota10,nota1))
                
                elif (pos3 == 5):
                    print("%.0f nota(s) de 100, %.0f nota(s) de 10 e %.0f nota(s) de 5." %(nota100,nota10,nota5))

                else:
                    print("%.0f nota(s) de 100, %.0f nota(s) de 10, %.0f nota(s) de 5 e %.0f nota de 1." %(nota100,nota10,nota5,nota1))
            
            elif (pos2 == 5):
                if (pos3 > 0) and (pos3 < 5):
                    print("%.0f nota(s) de 100, %.0f nota(s) de 50 e %.0f nota(s) de 1." %(nota100,nota50,nota1))
                
                elif (pos3 == 5):
                    print("%.0f nota(s) de 100, %.0f nota(s) de 50 e %.0f nota(s) de 5." %(nota100,nota50,nota5))

                else:
                    print("%.0f nota(s) de 100, %.0f nota(s) de 50, %.0f nota de 5 e %.0f nota de 1." %(nota100,nota50,nota5,nota1))
            
            else:
                if (pos3 > 0) and (pos3 < 5):
                    print("%.0f nota(s) de 100, %.0f nota(s) de 50, %.0f nota(s) de 10 e %.0f nota(s) de 1." %(nota100,nota50,nota10,nota1))
                
                elif (pos3 == 5):
                    print("%.0f nota(s) de 100, %.0f nota(s) de 50, %.0f nota(s) de 10 e %.0f nota(s) de 5." %(nota100,nota50,nota10,nota5))
                
                else:
                    print("%.0f nota(s) de 100, %.0f nota(s) de 50, %.0f nota(s) de 10, %.0f nota(s) de 5 e %.0f nota(s) de 1." %(nota100,nota50,nota10,nota5,nota1))
    
    else:
        print("6 notas de 100.")

else:    
    print("Valor incorreto para o saque!")
          





