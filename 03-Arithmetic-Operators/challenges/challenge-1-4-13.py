#Crie um programa que leia o valor informado e mostre quanto esse valor vale em doláres. Considerando 1 dolár: 3,27 reais.
name = input('Olá, por favor me fala o seu nome: ')
valueInReal = float(input('Oii, {}! Me fala um valor para que eu mostre quantos dolares você teria com esse mesmo valor: '.format(name)))
convertRealToDolar = (valueInReal / 3.27)
print('Shoow, {}! O valor que você me informou foi {:.2f} que equivale a {:.2f} em doláres.'.format(name, valueInReal, convertRealToDolar))
