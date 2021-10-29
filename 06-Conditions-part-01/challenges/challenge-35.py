# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

print('---ANO BISSEXTO---')
year = int(input('Olá, informe um ano para que eu verifique se ele é bissexto - informe "0" para o ano atual: '))

if year == 0:
    year = date.today().year

yearBi = year % 4 == 0 #Cálculo do ano bissexto!
yearBiNot = yearBi % 100 == 0 #Cálculo do ano quando não é bissexto
yearBiException = (yearBiNot % 400) == 0 # Cálculo do ano bissexto com exceção

if yearBiException:
    print('O ano {} que você informou é bissexto!'.format(year))
else:
    print('O ano {} que você informou não é bissexto!'.format(year))