
# Uma fruteira está vendendo frutas com a seguinte tabela de preços:

#                    Até 5 Kg             Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

pesomo = float(input("Informe a quantidade quilos de morango: "))
pesoma = float(input("Informe a quantidade quilos de maçã: "))
somapeso = pesomo + pesoma

if somapeso <= 5 and somapeso > 0:
    precomo = pesomo * 2.5
    precoma = pesoma * 1.8
    somapreco = precomo + precoma
    print("Preço do morango: R$ %.2f" %precomo)
    print("Preço da maçã: R$ %.2f" %precoma)
    print("%.2f kg no valor de R$ %.2f" %(somapeso,somapreco))

elif somapeso > 5:
    precomo = pesomo * 2.2
    precoma = pesoma * 1.5
    somapreco = precomo + precoma

    if (somapeso > 5 and somapeso < 8) and (somapreco <= 25):
        print("Preço do morango: R$ %.2f" %precomo)
        print("Preço da maçã: R$ %.2f" %precoma)
        print("%.2f kg no valor de R$ %.2f" %(somapeso,somapreco))
    elif somapeso >= 8 or somapreco > 25:
        desconto = somapreco * 0.1
        somapreco = somapreco - desconto
        print("Preço do morango: R$ %.2f" %precomo)
        print("Preço da maçã: R$ %.2f" %precoma)
        print("Valor do desconto: R$ %.2f" %desconto)
        print("%.2f kg no valor de R$ %.2f" %(somapeso,somapreco))

else:
    print("Valor incorreto.")



