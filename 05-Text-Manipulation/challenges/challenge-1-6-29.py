#Faça um programa que leia uma frase e mostre: quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez, em que posição ela aparece a última vez.
readPhrase = input('Olá, digite uma frase qualquer: ').upper().strip()
phraseLenght = readPhrase.count("A")
readPhrase = readPhrase.replace(" ", "")
phraseVerifyFirstA = readPhrase.find("A")
phraseVerifyLastA = readPhrase.rfind("A")
print("""
    A letra "A" aparece {} vezes \n
    A primeira letra "A" aparece na posição {}\n
    A última letra "A" aparece na posição {} 
""".format(phraseLenght, phraseVerifyFirstA+1, phraseVerifyLastA+1))
