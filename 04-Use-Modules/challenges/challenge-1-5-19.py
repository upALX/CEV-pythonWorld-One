#Crie um programa que lê um número do tipo real e mostre na tela a sua porção inteira. Ex: 4.32423 será 4.
import math
name = input('Olá, por favor me diga o seu nome: ')
intNumberFloor = float(input('Beleza, {}! Agora digita um número real pra que eu te mostre ele na sua versão inteira: '.format(name)))
print('Certo, {}. Você ne deu o número {} e ele equivale a {} na sua forma inteira.'.format(name, intNumberFloor, math.floor(intNumberFloor)))
