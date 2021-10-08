#Leia na tela o valor de um ângulo qualquer e mostre na tela o valor do seu SENO, COSCENO e TÂNGENTE.
from math import radians, cos, sin, tan
name = input('Olá novamente, por favor, me fala o seu nome: ')
ângulo = int(input('Beleza, {}! Agora me fala o valor do seu ângulo: '.format(name)))
seno = sin(radians(ângulo))
cosceno = cos(radians(ângulo))
tangente = tan(radians(ângulo))
print('Shoow, {}. Com base no ângulo de {} que você me passou, consegui calcular o seno igual a {:.3f}, cosceno igual a {:.3f}, tângente igual a {:.3f}. (resultados arredondados)'.format(name, ângulo, seno, cosceno, tangente))
