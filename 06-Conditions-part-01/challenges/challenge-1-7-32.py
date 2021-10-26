# Escreva um programa que vai ler a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem caso ultrapasse os 80Km/h dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por Km acima da média. Calcule o valor da multa e mostre junto da mensagem também.

print('A velocidade máxima é de 80Km/h! Caso ultrapasse terá multa de R$7,00 por Km infringido!')
currentSpeed = float(input('Olá, informe a sua velocidade atual: '))

if currentSpeed > 80:
    trafficTicketValue = (currentSpeed - 80) * 7
    print('Você está à {} Km/h, {} Km/h acima do limite!'.format(currentSpeed, currentSpeed - 80))
    print('Você deve pagar R$ {:.2f} de multa!'.format(trafficTicketValue))
else:
    print('Você está dentro do limite de velocidade, tenha um bom dia!')