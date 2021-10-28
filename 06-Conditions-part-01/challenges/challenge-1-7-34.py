# Desenvolva um programa que pergunte a distância de uma viagem por Km. Calcule o preço da passagem,
# cobrando R$ 0,50 por Km para viagens de até 200Km e R$ 0,45 para viagens mais longas.

distanceKm = float(input('Olá, me fala a distância da sua viagem em Km para o cálculo da passagem: '))
if distanceKm <= 200:
    valueTicket = distanceKm * 0.50
    print('Para {} Km a passagem é R$ {:.2f}! Crédito ou débito?'.format(distanceKm, valueTicket))
else:
    valueTicket = distanceKm * 0.45
    print('Para {} Km a passagem é R$ {:.2f}! Crédito ou débito?'.format(distanceKm, valueTicket))
