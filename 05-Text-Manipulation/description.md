#Anotações

- A função 'count()' - faz a contagem de strings (especificadas dentro do parenteses) dentro da cadeia de caracteres. 
- A função len() - faz a contagem do tamanho de uma variável armazenada.
- Toda variável é armazenada numa lista pela linguagem.
- O fatiamento de strings em Python funciona utilizando ':'. Ex: nome-da-variavel[onde-começa:onde-termina:de-quanto-em-quanto].
- Quando se faz fatiamento em Python, o número final do fatiamento não é contado. Ex: [0:13] - O que está armazenado na posição 13 não será incluído, apenas a anterior. Provavelmente porque a visualização é feita com base na contagem normal, e a busca é feita pelas posições dentro da lista, logo a posição 13 equivale em contagem ao elemento 12 da lista.
- A busca é feita com base em posição, já a visualização é feita por contagem de elemento na lista. Ex: 0 à 12 há 13 posições, quando se pede para mostrar de 0 à 12 o resultado é igual a 11, não 12. Isso acontece porque a forma de buscar é diferente da forma de mostrar. Você precisa buscar com base na posição, não com base na contagem porque senão sempre terá um resultado diferente do esperado inicialmente.
- A função 'find()' - Serve para você encontrar uma cadeia dentro da própria cadeia de caracteres. Ele sempre retorna a posição de inicio da cadeia que foi buscada.
- 'in' é um operador que retorna um Boolean falando se existe ou não determinado caractere, consjunto de caracteres ou numbers dentro da variável. Ex: frase = 'Curso em video' | Curso in frase 
- Uma lista de String é imutável, porém pode ser modificada através de métodos. O valor modificado só será salvo se for reatribuído a mesma variável, caso contrário a modificação ficará somente naquela instância onde se utilizou o método de modificação.
- Método 'replace()' - ele muda uma coisa por outra = replace('O que será modificado',''O que vai entrar no lugar') - O replace não substitui as coisas diretamente.
- Método 'upper()' - transforma toda cadeia em maiúscula.
- Método 'lower()' - transforma toda cadeia em minúsculas.
- Método 'capitalize()' - transforma toda cadeia em minúsculas, e depois transforma a primeira letra da cadeia inteira em MAIÚSCULA.
- Método 'title()' - analisa as palavras dentro da cadeia (com base nos espeços ele consegue identificar onde termina e começa uma palavra) e transforma cada letra inicial de cada palavra em MAIÚSCULA.
- Método 'strip()' - remove todos os espaços iniciais e finais de uma cadeia de caracteres.
- Método 'rstrip()' - remove somente os espaços do final da cadeia.
- Método 'lstrip()' - remove os espaços do inicio da cadeia.
- Método 'split()' - é feito em seus espaços, logo ele cria uma cadeia nova a cada espaço dentro da cadeia inicial. Ex: frase = 'curso em video' - com split(frase) - ele passa a armazenar frase em 3 listas ao ínves de uma e cada nova lista tem o seu número de referência (começa no 0).
- Método 'join()' - junta elementos com base em alguma coisa. Ex: '-'.join(frase) == curso-em-video

#Enunciados
- Crie um programa que leia o nome completo de uma pessoa e mostre: todas as letras em maiúsculas, todas as letras em minúsculas, quantas letras tem ao todos (sem considerar os espaços) e quantas letras tem o primeiro nome.
- Faça um programa que leia um número de 0 a 9.999 e mostre na tela cada um dos digitos separados. Ex: 1234 - unidade: 4, dezena: 3, centena: 2, milhar: 1.
- Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
- Crie um prorama que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
- Faça um programa que leia uma frase e mostre: quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez, em que posição ela aparece a última vez.
- Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
