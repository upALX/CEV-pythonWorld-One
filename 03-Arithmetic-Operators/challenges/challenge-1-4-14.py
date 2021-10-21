#Faça um programa que leia a largura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-lá, sabendo que cada litro de tinta, pinta uma área de 2m2.
name = input('Oii, novamente. Por favor, me fala o seu nome porque sou muito esquecido: ')
base = float(input('Beleza, {}! Me fala qual o tamanho da base da parede em metros: '.format(name)))
height = float(input('Beleza, {}! Me fala qual a altura da parede em metros: '.format(name)))
calcArea = (base * height)
calcInk = (calcArea / 2)
print('{} você me disse que tem uma base de {:.2f} metros e uma altura de {:.2f} metros, isso equivale a uma área de {:.2f} metros quadrados, logo você precisará de {:.2f} litros de tinta para pintar sua parede!'.format(name, base, height, calcArea, calcInk))
