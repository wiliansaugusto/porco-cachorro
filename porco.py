# -*- coding: utf-8 -*-
import sklearn
#tem perna curta, e gordinho , e faz late
porco1 = [1, 1, 0]
porco2 = [1, 1, 0]
porco3 = [1, 1, 0]
cachorro4 = [1, 1, 1]
cachorro5 = [0, 0, 1]
cachorro6 = [0, 1, 1]
dados = [porco1, porco2, porco3, cachorro4, cachorro5, cachorro6]
marcacoes = [1, 1, 1, -1, -1, -1]
from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()
modelo.fit(dados, marcacoes)
misterioso1 = [1, 1, 1]
misterioso2 = [1, 0, 0]
misterioso3 = [0, 1, 1]
misterioso4=  [1, 1, 1]
#cachorro , porco, cachorro
teste = [misterioso1,misterioso2, misterioso3]
resultado = modelo.predict(teste)
marcacoes_teste = [-1, 1, -1]
diferencas = resultado - marcacoes_teste
acertos = [d for d in diferencas if d == 0]

total_de_acertos = len(acertos)
total_de_elementos = len(teste)
taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

print("A taxa de acerto é de {}%".format(taxa_de_acerto))
index =0

for mostrar in resultado:
    if(resultado[index] == 1 ):
            animal="Porco"
    else:
            animal = "Cachorro"
            
    print("O animal  {} é um {}".format(index+1, animal))
    index+=1
