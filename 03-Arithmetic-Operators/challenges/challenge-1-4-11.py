#Escreva um programa que leia um valor em metros e o exiba em centimetros e milímetros.
name = input('Olá, por favor me fala o seu nome: ')
meterRequest = float(input('Beleza, {}. Agora me fala um número (vou considerar ele como metro) e vou mostrar ele para você em centimetros e milímetros: '.format(name)))
centimetersConvert = meterRequest * 100
milimitersConvert = meterRequest * 1000
print('Shoow, {}! Agora que você me disse o número {} posso te dizer que ele equivale a: {} centimetros e {} milímetros.'.format(name, meterRequest, centimetersConvert, milimitersConvert))
