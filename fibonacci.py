'''
Faça um programa que preencha um vetor de N elementos inteiros com a sequência de Fibonacci (primeiro
elemento é 1, segundo é 1 e em seguida, cada termo subsequente é a soma dos dois anteriores).
'''

print('Sequencia de Fibonnaci')
n = int(input('Quantos termos você quer mostrar?'))
n1 = 0
n2= 1
print('{} {}'.format(n1, n2), end='')
cont = 3
while cont <= n:
    n3 = n1 + n2
    print(' {}'.format(n3), end='')
    n1 = n2
    n2= n3
    cont += 1
