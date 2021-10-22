#Crie um prorama que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
namePearson = input('Olá, diga para mim o seu nome completo: ').strip().upper()
namePearsonCompair = namePearson.find("SILVA") > 0
print('Olá, você me informou o nome {}. Esse nome contém "Silva" no nome: {}'.format(namePearson.title(), namePearsonCompair))