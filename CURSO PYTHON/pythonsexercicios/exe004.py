s = input('Digite algo: ') #input sempre retorna o tipo string
print('O tipo primitivo deste valor é ', type(s))
print('Só tem espaços?', s.isspace())
print('É um numero? ', s.isnumeric())
print('É alfabetico:', s.isalpha())
print('É alfanumerico?', s.isalnum())
print('Esta em maiscula? ', s.isupper())
print('Esta em minuscula? ', s.islower())
print('Esta capatalizado? ', s.istitle())