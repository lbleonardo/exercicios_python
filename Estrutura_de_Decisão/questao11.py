
# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.

# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario = float(input("Informe o seu salário em R$: "))

if salario <= 280:
    ajuste = salario * 0.2
    novosalario = salario + ajuste
    print("Salário antes do ajuste: R$ %.2f" %salario)
    print("Percentual de aumento: 20%")
    print("Valor do aumento: R$ %.2f" %ajuste)
    print("Salário após o ajuste: R$ %.2f" %novosalario)

elif (salario > 280) and (salario <= 700):
    ajuste = salario * 0.15
    novosalario = salario + ajuste
    print("Salário antes do ajuste: R$ %.2f" %salario)
    print("Percentual de aumento: 15%")
    print("Valor do aumento: R$ %.2f" %ajuste)
    print("Salário após o ajuste: R$ %.2f" %novosalario)

elif (salario > 700) and (salario <= 1500):
    ajuste = salario * 0.10
    novosalario = salario + ajuste
    print("Salário antes do ajuste: R$ %.2f" %salario)
    print("Percentual de aumento: 10%")
    print("Valor do aumento: R$ %.2f" %ajuste)
    print("Salário após o ajuste: R$ %.2f" %novosalario)

else:
    ajuste = salario * 0.05
    novosalario = salario + ajuste
    print("Salário antes do ajuste: R$ %.2f" %salario)
    print("Percentual de aumento: 5%")
    print("Valor do aumento: R$ %.2f" %ajuste)
    print("Salário após o ajuste: R$ %.2f" %novosalario)

