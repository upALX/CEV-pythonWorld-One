#Desenvolva um programa que leia as duas notas de um aluno e calcule a média.
name = input('Olá, me fala o seu nome, por favor: ')
noteOne = float(input('Oii {}, por favor me fala a primeira nota: '.format(name)))
noteTwo = float(input('Perfeito {}, agora me fala a segunda nota: '.format(name)))
print('Beleza, {}. A média das notas: {} e {} é igual a {}. '.format(name, noteOne, noteTwo, (noteOne+noteTwo)/2))
