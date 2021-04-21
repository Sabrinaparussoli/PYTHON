n = int(input('Digite um numero: '))
d = n * 2
t = n * 3
r = n**(1/2)
print('O dobro do valor de {} é: {}'.format(n, d))
print('O triplo do valor de {} é: {}'.format(n, t))
print('A raiz do valor de {} é: {:.2f}'.format(n, r))

# outra possibilidade
n = int(input('Digite um numero: '))

print('O dobro do valor de {} é: {}'.format(n, (n*2)))
print('O triplo do valor de {} é: {}'.format(n, (n*3)))
print('A raiz do valor de {} é: {:.2f}'.format(n, pow(n,(1/2))))