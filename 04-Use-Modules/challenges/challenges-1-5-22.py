#Um professor quer sortear um de seus 4 alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dele e escrevendo o nome escolhido.
import random
nameTeacher = input('Olá, caro professor, por favor informe o seu número para liberar o sorteio: ')
nameOne = input('{}, por favor me diz o nome do seu primeiro aluno: '.format(nameTeacher))
nameTwo = input('{}, por favor me diz o nome do seu segundo aluno: '.format(nameTeacher))
nameThree = input('{}, por favor me diz o nome do seu terceiro aluno: '.format(nameTeacher))
nameFour = input('{}, por favor me diz o nome do seu quarto aluno: '.format(nameTeacher))
listAlumni = [nameOne, nameTwo, nameThree, nameFour]
randomChoise = random.choice(listAlumni)
print('Certo, {}. De todos os alunos, o escolhido foi esse aqui: {}.'.format(nameTeacher, randomChoise))
