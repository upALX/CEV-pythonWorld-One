#Faça um programa que leia um número de 0 a 9.999 e mostre na tela cada um dos digitos separados.
#Ex: 1234 - unidade: 4, dezena: 3, centena: 2, milhar: 1.
numberConvert = int(input('Olá, por favor informe um número dê 0 à 9.999: '))
unidadeConverted = numberConvert // 1 % 10
dezenaConverted = numberConvert // 10 % 10
centenaConverted = numberConvert // 100 % 10
milharConverted = numberConvert // 1000 % 10

print('A unidade é {}'.format(unidadeConverted))
print('A dezena é {}'.format(dezenaConverted))
print('A centena é {}'.format(centenaConverted))
print('O milhar é {}'.format(milharConverted))
