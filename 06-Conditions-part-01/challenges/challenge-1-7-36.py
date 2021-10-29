# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

numberOne = int(input('Olá, informe o primeiro número para a comparação: '))
numberTwo = int(input('Olá, informe o segundo número para a comparação:'))
numberThree = int(input('Olá, informe o terceiro número para a comparação:'))

numbers = [numberOne, numberTwo, numberThree]

print('Após os valores informados, percebi que o maior é {}!'.format(max(numbers)))
print('Após os valores informados, percebi que o menor é {}!'.format(min(numbers)))
