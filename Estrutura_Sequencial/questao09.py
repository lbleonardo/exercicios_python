# Exercício Estrutura Sequencial

# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).

tempF = float(input("Informe a temperatura em graus Fahremheit: "))
tempC = 5 * ((tempF-32) / 9)

print("A temperatura em graus Celsius é %.0f." %tempC)
