# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.
print('---PAR OU ÍMPAR---')
numberReading = int(input('Olá, me fala um número que não seja negativo: '))
if numberReading % 2 == 0:
    print('{} é par!'.format(numberReading))
else:
    print('{} é ímpar!'.format(numberReading))
