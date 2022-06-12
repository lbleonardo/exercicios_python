
# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" 

# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

q1 = input("Telefonou para a vítima (S ou N)? ")
q2 = input("Esteve no local do crime (S ou N)? ")
q3 = input("Mora perto da vítima (S ou N)? ")
q4 = input("Devia para a vítima (S ou N)? ")
q5 = input("Já trabalhou com a vítima (S ou N)? ")

if q1 == 'S' or q1 == 's':
    q1 = 1

if q1 == 'N' or q1 == 'n':
    q1 = 0

if q2 == 'S' or q2 == 's':
    q2 = 1

if q2 == 'N' or q2 == 'n':
    q2 = 0

if q3 == 'S' or q3 == 's':
    q3 = 1

if q3 == 'N' or q3 == 'n':
    q3 = 0

if q4 == 'S' or q4 == 's':
    q4 = 1

if q4 == 'N' or q4 == 'n':
    q4 = 0

if q5 == 'S' or q5 == 's':
    q5 = 1

if q5 == 'N' or q5 == 'n':
    q5 = 0

soma = q1 + q2 + q3 + q4 + q5

if soma == 2:
    print("Suspeita.")

elif soma >= 3 and soma <= 4:
    print("Cúmplice.")

elif soma == 5:
    print("Assassino.")

else:
    print("Inocente.")
