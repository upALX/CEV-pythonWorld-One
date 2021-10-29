# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

print('---ANO BISSEXTO---')
yearBi = int(input('Olá, informe um ano para que eu verifique se ele é bissexto: '))
yearBiCalc = yearBi % 100 == 0
yearBiNot = (yearBiCalc % 400) == 0
if yearBiNot:
    print('Bissexto!')
else:
    print('Não é bissexto!')