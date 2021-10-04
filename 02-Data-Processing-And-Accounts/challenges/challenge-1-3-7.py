#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

name = input('Oii, você gosta mesmo daqui, né? Antes de mais nada me fala o seu nome: ')
discoverTypesUser = input('Certo, {}! Agora digita alguma coisa pra que eu fale para você curiosidades sobre o que foi digitado: '.format(name))
print('O tipo de dado do que foi digitado é: {}.'.format(type(discoverTypesUser)))
print('Foi digitado somente espaço: {}.'.format(discoverTypesUser.isspace()))
print('É um número ou pode ser convertido em número: {}.'.format(discoverTypesUser.isnumeric()))
print('É ou pode ser convertido em String: {}.'.format(discoverTypesUser.isalpha()))
print('Contém números e letras (alfanúmerico): {}.'.format(discoverTypesUser.isalnum()))
print('Está num formato de somente letras maiúsculas: {}.'.format(discoverTypesUser.isupper()))
print('Está num formato de somente letras minúsculas: {}.'.format(discoverTypesUser.islower()))
print('Está num formato que não é nem somente maiúsculas nem somente minúsculas, mas uma mescla de ambos os formatos: {}.'.format(discoverTypesUser.istitle()))

