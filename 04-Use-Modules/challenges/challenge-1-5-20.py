#Faça um programa que leia o comprimento do cateto oposto e adjacente de um triângulo , calcule e mostre o comprimento da hipotenusa.
#Ou seja: calcule o valor da hipotenusa.
from math import hypot
name = input('Olá, me fala o seu nome: ')
catetoOposto = float(input('Shoow, {}! Agora me fala qaunto vale o seu cateto oposto: '.format(name)))
catetoAdjacente = float(input('Belza, {}! Agora me fala quanto vale o seu cateto adjacente: '.format(name)))
valueHipotenusa = hypot(catetoOposto, catetoAdjacente)
print('{} com base nos dados que você me passou, seu cateto oposto vale {} e o adjacente vale {}, logo sua hipotenusa equivale a {:.3f}.'.format(name, catetoOposto, catetoAdjacente, valueHipotenusa))
