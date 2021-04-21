print('-'*12, 'PINTANDO PAREDE', '-'*12)

h = float(input('Qual a altura da parede em metros: '))
l = float(input('Qual a largura da parede em metros: '))
a = h * l
pintura = a / 2
print('A sua parede tem a dimensão de {:.2f} x {:.2f} e sua area é de {:.2f}m2'.format(h, l, a))
print('Para pinta essa parede, vc irá precisa de {}l de tinta'.format(pintura))