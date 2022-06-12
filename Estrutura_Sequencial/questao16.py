# Exercício Estrutura Sequencial

# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

area = int(input("Informe a área em metros quadrados a ser pintada: "))
areaLata = 54
precoLata = 80

if area > areaLata:
    qtdLata = area / areaLata
    if (area % areaLata) == 0:
        precoT = qtdLata * precoLata
        print("Quantidade total de latas: %.0f" %qtdLata)
        print("Preço total: R$ %.2f" %precoT)
    else:
        qtdLata = area // areaLata
        qtdLata += 1
        precoT = qtdLata * precoLata
        print("Quantidade total de latas: %.0f" %qtdLata)
        print("Preço total: R$ %.2f" %precoT)
else:
    print("Quantidade total de latas: 1")
    print("Preço total: R$ 80.00")


    
          
    