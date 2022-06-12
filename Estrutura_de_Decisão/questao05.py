
# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))

media = (nota1 + nota2) / 2

if (media >= 7) and (media < 10):
    print("Sua média foi %.2f e você foi APROVADO!" %media)
elif media == 10:
    print("Sua média foi %.2f e você foi APROVADO COM DISTINÇÃO!" %media)
else:
    print("Sua média foi %.2f e você foi REPROVADO!" %media)
