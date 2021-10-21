# Crie um programa que leia o nome completo de uma pessoa e mostre: todas as letras em maiúsculas,
# todas as letras em minúsculas, quantas letras tem ao
# todo sem considerar os espaços e quantas letras tem o primeiro nome.
name = input('Olá, me fala o seu nome completo por favor: ')
print(
"""{}, seu nome em MAIÚCULAS É {}, 
    em minúsculas é {},
    seu nome completo possui {} letras,
    e o primeiro nome possui {} letras.
""".format(name, name.upper(), name.lower(), len(name.replace(" ", "")), len(name.split()[0])))
