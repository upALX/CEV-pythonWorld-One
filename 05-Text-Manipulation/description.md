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

#Pós realização de exercícios:
- Sempre devo fazer o desafio dividido em êtapas menores e testando cada êtapa porque se deixar para testar depois de pronto e tiver um erro, encontra-lo vai ser 10x mais complicado.
- É IMPORTÂNTE ENTENDER QUE O LENGHT QUANDO UTILIZADO PARA REPRESENTAR UMA POSIÇÃO, IRÁ RETORNAR UM VALOR ACIMA DO ESPERADO, JÁ QUE ELE FAZ A BUSCA COM BASE EM ELEMENTOS - inicia em 1, não em 0 - NÃO NAS POSIÇÕES DOS ELEMENTOS. 
- O lenght faz meio que essa ideia: "existe uma coisa aqui, existem duas coisas aqui...".
- O find por exemplo, já faz o seguinte: "dentro dessa coisa que existe ai, tem a algo na posição 0, tem algo na posição 1, tem algo na posição 2..."
- Para o lenght é necessário dizer que existe algo, por isso ele precisa retornar o 1 quando existe algo e faz a contagem a partir disso, afinal ele não procura coisas dentro de uma coisa, mas ele procura a existencia de algo, e a existencia de algo precisa ser maior que zero logicamente, não é mesmo?

#Enunciados
- Crie um programa que leia o nome completo de uma pessoa e mostre: todas as letras em maiúsculas, todas as letras em minúsculas, quantas letras tem ao todos (sem considerar os espaços) e quantas letras tem o primeiro nome.
- Faça um programa que leia um número de 0 a 9.999 e mostre na tela cada um dos digitos separados. Ex: 1234 - unidade: 4, dezena: 3, centena: 2, milhar: 1.
- Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
- Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
- Faça um programa que leia uma frase e mostre: quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez, em que posição ela aparece a última vez.
- Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
- Faça um programa que leia o nome completo de uma pessoas, mostrando em seguida o primeiro e o último nome separadamente.