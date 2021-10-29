# Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se podem ou não formar um triângulo.

valueOne = int(input('Informe o valor da primeira reta: '))
valueTwo = int(input('Informe o valor da segunda reta:'))
valueThree = int(input('Informe o valor da terceira reta:'))

straight = [valueOne, valueTwo, valueThree]
orderedStraight = sorted(straight)

valueMin = orderedStraight[0]
valueMedium = orderedStraight[1]
valueMax = orderedStraight[2]

if valueMin + valueMedium > valueMax:
    print('As retas informadas formam um triângulo!')
else:
    print('As retas informadas não formam um triângulo!')
