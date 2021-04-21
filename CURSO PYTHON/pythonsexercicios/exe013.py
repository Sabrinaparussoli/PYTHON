s = float(input('Qual é o salario do funcionario R$ '))
novo = s + (s * 15 / 100)
print('Um funcionario que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(s, novo))