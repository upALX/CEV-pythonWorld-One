#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro e mostre a ordem sorteada.
from random import shuffle
nameTeacher = str(input('Olá professor, por favor me fala o seu nome para liberar o sorteio: '))
nameOne = str(input('{} me fala o nome do primeiro aluno: '.format(nameTeacher)))
nameTwo = str(input('{} me fala o nome do primeiro aluno: '.format(nameTeacher)))
nameThree = str(input('{} me fala o nome do primeiro aluno: '.format(nameTeacher)))
nameFour = str(input('{} me fala o nome do primeiro aluno: '.format(nameTeacher)))
listAlumni = [nameOne, nameTwo, nameThree, nameFour]
shuffle(listAlumni)
print(listAlumni)
