# Exercício Estrutura Sequencial

# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    # comprar apenas latas de 18 litros;
    # comprar apenas galões de 3,6 litros;
    # misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

metrolitro = 6
litrolata = 18
precolata = 80
arealata = litrolata * metrolitro
litrogalao = 3.6
precogalao = 25
areagalao = litrogalao * metrolitro

area = int(input("Area: "))
escolha = input("Tipo de compra: (L)ata, (G)alão ou (M)isto: ")

if (escolha == "L") or (escolha == "l"):
    if area > arealata:
        qtdlata = area / arealata    
        if area % arealata == 0:
            precotl = qtdlata * precolata
            print("Latas:", qtdlata, "Preço: R$", precotl)
        else:
            qtdlata = (area // arealata) + 1
            precotl = qtdlata * precolata
            print("Latas:", qtdlata, "Preço: R$", precotl)
    else:
        qtdlata = 1
        print("Latas:", qtdlata, "Preço: R$", precolata)

elif (escolha == "G") or (escolha == "g"):
    if area > areagalao:
        qtdgalao = area / areagalao
        if area % areagalao == 0:
            precotg = qtdgalao * precogalao
            print("Galões:", qtdgalao, "Preço: R$", precotg)
        else:
            qtdgalao = (area // areagalao) + 1
            precotg = qtdgalao * precogalao
            print("Galões:", qtdgalao, "Preço R$:", precotg)

elif (escolha == "M") or (escolha == "m"):
    if area % arealata != 0:
        qtdlata = area // arealata
        precotl = qtdlata * precolata
        arearestg = area % arealata
        qtdgalao = arearestg / areagalao
        if arearestg <= 64:
            if arearestg % areagalao == 0:
                precotg = qtdgalao * precogalao
                print("Qtd Latas:", qtdlata, " / Preco Total Latas: R$", precotl)
                print("Qtd Galões:", qtdgalao, " / Preco Total Galões: R$", precotg)
                print("Preço total (latas + galões) R$", precotl + precotg)
            else:
                qtdgalao = (arearestg // areagalao) + 1
                precotg = qtdgalao * precogalao
                print("Qtd Latas:", qtdlata, " / Preco Total Latas: R$", precotl)
                print("Qtd Galões:", qtdgalao, " / Preco Total Galões: R$", precotg)
                print("Preço total (latas + galões) R$", precotl + precotg)
        else:
            qtdlata += 1
            precotl = qtdlata * precolata
            print("Qtd Latas:", qtdlata, " / Preco Total Latas: R$", precotl)                                      

else:
    print("Erro, insira o valor corretamente!!!")
