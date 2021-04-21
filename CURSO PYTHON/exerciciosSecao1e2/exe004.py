x = 0
soma = 0
i = 0
while x != -1:
   x = int(input('digite uma idade: '))
   if x != -1:
       soma += x
       i += 1
print(soma/i)