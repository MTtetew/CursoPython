1) Escreva um algoritmo que armazene o valor 10 em uma variável A e o valor 20 em uma variável B. A seguir (utilizando apenas atribuições entre variáveis) troque os seus conteúdos fazendo com que o valor que está em A passe para B e vice-versa. Ao final, escrever os valores que ficaram armazenados nas variáveis.



A=10
B=20

print(A,"valor A")
print(B,"valor B")
temporario=A
A=B
B=temporario

print(A,"valor A")
print(B,"valor B")
