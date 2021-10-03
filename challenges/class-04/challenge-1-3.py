#Crie um script Python que leia dois números e mostre a soma entre eles.

print('Olá, você está tentando fazer uma soma, não é mesmo? Então, vamos lá!')
name = input('Antes de tudo, me fala o seu nome, por favor: ')
valueOne = input('Beleza, agora me fala o primeiro número que quer somar: ')
valueTwo = input('E agora me fala o segundo número que deseja somar: ')
soma = int(valueOne) + int(valueTwo)
print('Tá feito ' +name+ '! A soma de ' +valueOne+ ' com ' +valueTwo+ ' é igual a ', soma, '!')
