#Faça um programa que leia o nome completo de uma pessoas, mostrando em seguida o primeiro e o último nome separadamente.
nameComplete = input('Olá, por favor me fala o seu nome completo: ').strip().title()
nameDivided = nameComplete.split()
lenghtList = len(nameDivided)
print('Seu nome completo é: {}'.format(nameComplete))
print('Seu primeiro nome é: {}'.format(nameDivided[0]))
print('Seu último nome é: {}'.format(nameDivided[len(nameDivided)-1])) #O lenght retorna a existencia, não a posição.

