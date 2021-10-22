#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
nameCity = input('Olá, me fala uma cidade e caso ela comece com a palavra "SANTO" vou dizer "True", caso contrário direi "False": ').upper()
nameValid = nameCity.split()[0] == "SANTO"
print('Você me falou a cidade {}. Essa cidade começa com a palavra "SANTO": {}'.format(nameCity, nameValid))
