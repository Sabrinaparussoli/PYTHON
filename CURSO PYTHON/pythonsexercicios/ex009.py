n = int(input('Digite um numero para ver sua tabuada: '))
print('-'*12)
for i in range(0,11):
    print('{} * {} = {}'.format(n, i, n*i))
print('-'*12)