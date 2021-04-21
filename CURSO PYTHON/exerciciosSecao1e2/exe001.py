peso = [] # // criando uma lista para armazenar o conteudo digitado
cont = 0 #//contador que irá passar para o proximo peso
for i in range (0, 7): #//estrutura de repetição
    peso.append(float(input('Digite um peso:'))) #// append irá inserir um novo elemento no final da lista
    if peso[i] > 90:
        cont += 1
#// cont vai puxar a quantidade de pessoas acima do peso de 90, sum vai somar os pessos dividindo por len que esta retornando a quantidade de pesos digitados
print(f'existem {cont} pessoas acima do peso de 90kg e media de todos os pesos é {sum(peso)/len(peso):.2f}') #//:.2f limita o numero de casas após a virgula