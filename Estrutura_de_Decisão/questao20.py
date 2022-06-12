
# Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if (nota1 >= 0) and (nota1 <= 10) and (nota2 >= 0) and (nota2 <= 10) and (nota3 >= 0) and (nota3 <= 10):

    if media >= 7 and media <= 9.9:
        print("Sua média foi %.2f e você foi APROVADO!" %media)
    elif media == 10:
        print("Sua media foi %.2f e você foi APROVADO com DISTINÇÃO!" %media)
    else:
        print("Sua média foi %.2f e você foi REPROVADO!" %media)
else:
    print("Valor incorreto, a nota deve ser um número entre 0 e 10.")