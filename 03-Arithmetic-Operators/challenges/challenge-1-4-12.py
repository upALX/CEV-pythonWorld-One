#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
name = input('Olá, me fala o seu nome, por favor :) ')
timeTables = int(input('Beleza, {}! Me fala um número qualquer para que eu te fale a tabuada dele até 10: '.format(name)))
timeTableZero = timeTables * 0
timeTableOne = timeTables * 1
timeTableTwo = timeTables * 2
timeTableThree = timeTables * 3
timeTableFour = timeTables * 4
timeTableFive = timeTables * 5
timeTableSix = timeTables * 6
timeTableSeven = timeTables * 7
timeTableEight = timeTables * 8
timeTableNine = timeTables * 9
timeTableTen = timeTables * 10

print('{} sua tabuada está pronta: \n {}x0 = {} \n {}x1 = {} \n {}x2 = {} \n {}x3 = {} \n {}x4 = {} \n {}x5 = {} \n {}x6 = {} \n {}x7 = {} \n {}x8 = {} \n {}x9 = {} \n {}x10 = {} \n'.format(name, timeTables, timeTableZero, timeTables, timeTableOne, timeTables, timeTableTwo, timeTables, timeTableThree, timeTables, timeTableFour, timeTables, timeTableFive, timeTables, timeTableSix, timeTables, timeTableSeven, timeTables, timeTableEight, timeTables, timeTableNine, timeTables, timeTableTen))
#Esse é o jeito mais difícil, porém o melhor para se praticar!