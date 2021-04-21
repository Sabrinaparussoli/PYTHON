real = float(input('Quanto de dinheiro vc tem em sua carteira? R$'))
dolar = real / 5.62
novoSol = real / 1.56
print('Com R${:.2f} reais, vc pode comprar US${:.2f} dolar'.format(real, dolar))
print('Com R${:.2f} reais, vc pode comprar PEN{:.2f} PEN'.format(real, novoSol))