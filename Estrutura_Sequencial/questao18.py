# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanhoarq = float(input("Informe o tamanho do arquivo em MB: "))
veloint = float(input("Informe a velocidade do link em Mbps: "))

mbyteps = veloint / 8
tempodown = tamanhoarq / mbyteps

if (tamanhoarq % mbyteps != 0):
    minutos = int(tempodown)
    segundos = (tempodown - minutos) * 60
    print("O tempo de download é de %.0f minutos e %.0f segundos." %(minutos, segundos))
else:        
    print("O tempo de download é de %.0f minuto(s)." %tempodown)
