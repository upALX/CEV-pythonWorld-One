#Faça um programa que leia um número na tela e mostre na tela o seu sucessor e seu antecessor.
name = input('Olá, como você gosta mesmo de estar comigo preciso saber o seu nome: ')
sucessorAntecessor = int(input('E aí, {}! Quer ver eu te mostrar os números que vem antes e depois de qualquer número que você me disser? Beleza, então me fala um número: '.format(name)))
print('{} o número que você me mostrou foi o {}, o número que vem antes dele é o {}, e o número que vem depois dele é o {}.'.format(name, sucessorAntecessor, sucessorAntecessor-1, sucessorAntecessor+1))
