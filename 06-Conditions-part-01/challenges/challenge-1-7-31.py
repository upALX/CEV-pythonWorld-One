# Escreva um programa que faça o computador pensar num número entre 0 e 5, e peça para o usuário -
# tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

print("Olá, pensei num número!")
numberRight = randint(0, 5)
numberKicked = int(input("Me fala um número inteiro de 0 à 5 e vamos ver se você acerta o número que eu pensei: "))
if numberRight == numberKicked:
    print('Você venceu, o número chatado foi {} e o número que pensei foi {} também :)'.format(numberKicked, numberRight))
else:
    print('Você perdeu, o número chutado foi {} e o número que pensei foi {}, que pena!'.format(numberKicked, numberRight))

print('---FIM---')