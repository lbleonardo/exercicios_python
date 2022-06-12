
# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

#                    Até 5 Kg             Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

tipoc = input("Informe o tipo de carne: (F)filé duplo, (A)alcatra, (P)picanha: ")
quilosc = float(input("Informe a quantidade de quilos de carne: "))
tipopag = input("Pagamento em cartão (S ou N)? ")

if tipoc == 'F' or tipoc == 'f':
    if quilosc > 0 and quilosc <= 5:
        precoc = quilosc * 4.90
        if tipopag == 'S' or tipopag == 's':
            desconto = precoc * 0.05
            precodesc = precoc - desconto
            print("Tipo de carne: Filé Duplo")
            print("Quantidade: %.2f kg" %quilosc)
            print("Preço Total: R$ %.2f" %precoc)
            print("Tipo de pagamento: Cartão.")
            print("Valor Desconto: R$ %.2f" %desconto)
            print("Valor a pagar: R$ %.2f" %precodesc)
        
        elif tipopag == 'N' or tipopag == 'n':
            print("Tipo de carne: Filé Duplo")
            print("Quantidade: %.2f kg" %quilosc)
            print("Preço Total: R$ %.2f" %precoc)
            print("Tipo de pagamento: Dinheiro")
            print("Valor Desconto: R$ 0.00")
            print("Valor a pagar: R$ %.2f" %precoc)
    
    elif quilosc > 5:
        precoc = quilosc * 5.8
        if tipopag == 'S' or tipopag == 's':
            desconto = precoc * 0.05
            precodesc = precoc - desconto
            print("Tipo de carne: Filé Duplo")
            print("Quantidade: %.2f kg" %quilosc)
            print("Preço Total: R$ %.2f" %precoc)
            print("Tipo de pagamento: Cartão.")
            print("Valor Desconto: R$ %.2f" %desconto)
            print("Valor a pagar: R$ %.2f" %precodesc)
        
        elif tipopag == 'N' or tipopag == 'n':
            print("Tipo de carne: Filé Duplo")
            print("Quantidade: %.2f kg" %quilosc)
            print("Preço Total: R$ %.2f" %precoc)
            print("Tipo de pagamento: Dinheiro")
            print("Valor Desconto: R$ 0.00")
            print("Valor a pagar: R$ %.2f" %precoc)

elif tipoc == 'A' or tipoc == 'a':
    if quilosc > 0 and quilosc <= 5:
        precoc = quilosc * 5.90
        if tipopag == 'S' or tipopag == 's':
            desconto = precoc * 0.05
            precodesc = precoc - desconto
            print("Tipo de carne: Alcatra")
            print("Quantidade: %.2f kg" %quilosc)
            print("Preço Total: R$ %.2f" %precoc)
            print("Tipo de pagamento: Cartão.")
            print("Valor Desconto: R$ %.2f" %desconto)
            print("Valor a pagar: R$ %.2f" %precodesc)
        
        elif tipopag == 'N' or tipopag == 'n':
            print("Tipo de carne: Alcatra")
            print("Quantidade: %.2f kg" %quilosc)
            print("Preço Total: R$ %.2f" %precoc)
            print("Tipo de pagamento: Dinheiro")
            print("Valor Desconto: R$ 0.00")
            print("Valor a pagar: R$ %.2f" %precoc)

    elif quilosc > 5:
        precoc = quilosc * 6.8
        if tipopag == 'S' or tipopag == 's':
            desconto = precoc * 0.05
            precodesc = precoc - desconto
            print("Tipo de carne: Alcatra")
            print("Quantidade: %.2f kg" %quilosc)
            print("Preço Total: R$ %.2f" %precoc)
            print("Tipo de pagamento: Cartão.")
            print("Valor Desconto: R$ %.2f" %desconto)
            print("Valor a pagar: R$ %.2f" %precodesc)
        
        elif tipopag == 'N' or tipopag == 'n':
            print("Tipo de carne: Alcatra")
            print("Quantidade: %.2f kg" %quilosc)
            print("Preço Total: R$ %.2f" %precoc)
            print("Tipo de pagamento: Dinheiro")
            print("Valor Desconto: R$ 0.00")
            print("Valor a pagar: R$ %.2f" %precoc)

elif tipoc == 'P' or tipoc == 'p':
    if quilosc > 0 and quilosc <= 5:
        precoc = quilosc * 6.9
        if tipopag == 'S' or tipopag == 's':
            desconto = precoc * 0.05
            precodesc = precoc - desconto
            print("Tipo de carne: Picanha")
            print("Quantidade: %.2f kg" %quilosc)
            print("Preço Total: R$ %.2f" %precoc)
            print("Tipo de pagamento: Cartão.")
            print("Valor Desconto: R$ %.2f" %desconto)
            print("Valor a pagar: R$ %.2f" %precodesc)
        
        elif tipopag == 'N' or tipopag == 'n':
            print("Tipo de carne: Picanha")
            print("Quantidade: %.2f kg" %quilosc)
            print("Preço Total: R$ %.2f" %precoc)
            print("Tipo de pagamento: Dinheiro")
            print("Valor Desconto: R$ 0.00")
            print("Valor a pagar: R$ %.2f" %precoc)
    
    elif quilosc > 5:
        precoc = quilosc * 7.8
        if tipopag == 'S' or tipopag == 's':
            desconto = precoc * 0.05
            precodesc = precoc - desconto
            print("Tipo de carne: Picanha")
            print("Quantidade: %.2f kg" %quilosc)
            print("Preço Total: R$ %.2f" %precoc)
            print("Tipo de pagamento: Cartão.")
            print("Valor Desconto: R$ %.2f" %desconto)
            print("Valor a pagar: R$ %.2f" %precodesc)
        
        elif tipopag == 'N' or tipopag == 'n':
            print("Tipo de carne: Picanha")
            print("Quantidade: %.2f kg" %quilosc)
            print("Preço Total: R$ %.2f" %precoc)
            print("Tipo de pagamento: Dinheiro")
            print("Valor Desconto: R$ 0.00")
            print("Valor a pagar: R$ %.2f" %precoc)
