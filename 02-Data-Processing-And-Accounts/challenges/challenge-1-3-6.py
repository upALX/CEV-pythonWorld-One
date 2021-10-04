#Crie um programa que leia dois números e mostre a soma entre eles.
name = input('Olá, é ótimo ver você por aqui, agora me fala o seu nome: ')
valueOne = int(input('Beleza, '+ name + ' ! Agora preciso que me diga um número para somar: '))
valueTwo = int(input('Perfeito, ' + name + '! Agora me fala mais um número para somar: '))
sum: int = valueOne + valueTwo

print('Falaa, {}! A soma entre {} e {} da um total de {}'.format(name, valueOne, valueTwo, sum))
