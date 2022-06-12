
# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

 # Salário Bruto: (5 * 220)        : R$ 1100,00
 #       (-) IR (5%)                     : R$   55,00  
 #       (-) INSS ( 10%)                 : R$  110,00
 #       FGTS (11%)                      : R$  121,00
 #       Total de descontos              : R$  165,00
 #       Salário Liquido                 : R$  935,00


valorhora = float(input("Informe o valor da hora trabalhada em R$: "))
qtdhorames = int(input("Informe a quantidade de horas trabalhadas no mês: "))
salbruto = valorhora * qtdhorames

if (salbruto <= 900):
    inss = salbruto * 0.1
    fgts = salbruto * 0.11
    sindicato = salbruto * 0.03
    descontos = inss + sindicato
    salliquido = salbruto - descontos
    
    print("Salário Bruto: R$ %.2f" %salbruto)
    print("IR: ISENTO")
    print("INSS: R$ %.2f" %inss)
    print("FGTS: R$ %.2f" %fgts)
    print("Sindicato: R$ %.2f" %sindicato)
    print("Descontos: R$ %.2f" %descontos)
    print("Salário Líquido: R$ %.2f" %salliquido)

elif (salbruto > 900) and (salbruto <= 1500):
    ir = salbruto * 0.05
    inss = salbruto * 0.1
    fgts = salbruto * 0.11
    sindicato = salbruto * 0.03
    descontos = ir + inss + sindicato
    salliquido = salbruto - descontos
    
    print("Salário Bruto: R$ %.2f" %salbruto)
    print("IR: R$ %.2f" %ir)
    print("INSS: R$ %.2f" %inss)
    print("FGTS: R$ %.2f" %fgts)
    print("Sindicato: R$ %.2f" %sindicato)
    print("Descontos: R$ %.2f" %descontos)
    print("Salário Líquido: R$ %.2f" %salliquido)

elif (salbruto > 1500) and (salbruto <= 2500):
    ir = salbruto * 0.1
    inss = salbruto * 0.1
    fgts = salbruto * 0.11
    sindicato = salbruto * 0.03
    descontos = ir + inss + sindicato
    salliquido = salbruto - descontos
    
    print("Salário Bruto: R$ %.2f" %salbruto)
    print("IR: R$ %.2f" %ir)
    print("INSS: R$ %.2f" %inss)
    print("FGTS: R$ %.2f" %fgts)
    print("Sindicato: R$ %.2f" %sindicato)
    print("Descontos: R$ %.2f" %descontos)
    print("Salário Líquido: R$ %.2f" %salliquido)

else:    
    ir = salbruto * 0.2
    inss = salbruto * 0.1
    fgts = salbruto * 0.11
    sindicato = salbruto * 0.03
    descontos = ir + inss + sindicato
    salliquido = salbruto - descontos
    
    print("Salário Bruto: R$ %.2f" %salbruto)
    print("IR: R$ %.2f" %ir)
    print("INSS: R$ %.2f" %inss)
    print("FGTS: R$ %.2f" %fgts)
    print("Sindicato: R$ %.2f" %sindicato)
    print("Descontos: R$ %.2f" %descontos)
    print("Salário Líquido: R$ %.2f" %salliquido)

