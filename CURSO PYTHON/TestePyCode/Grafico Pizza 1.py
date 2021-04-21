import matplotlib.pyplot as plt
import numpy as np

#valores do grafico#
y = np.array([35,25,25,15])

#itens do grafico#
mylabels = ['a', 'b', 'c', 'd']

#espaço entre as "fatias" do grafico#
myexplode = [0,0,0,0]

#monta o grafico e depois mostra na tela#
plt.pie(y, labels=mylabels, explode=myexplode, shadow=True)
plt.show()

