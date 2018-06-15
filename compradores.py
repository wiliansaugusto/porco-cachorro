# -*- coding: utf-8 -*-
import csv

X = []
Y = []

arquivo = open('/home/pi/exemplos_python/acesso.csv', 'r')
leitor = csv.reader(arquivo)
next(leitor)

for acessou_home,acessou_como_funciona,acessou_contato, comprou in leitor:

    X.append([int(acessou_home),int(acessou_como_funciona),int(acessou_contato)])
    Y.append(int(comprou))
treino_dados = X[:90]
treino_marcacoes = Y[:90]

teste_dados = X[-9:]
teste_marcacoes = Y[-9:]

from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()
modelo.fit(treino_dados, treino_marcacoes)

resultado = modelo.predict(teste_dados)

diferencas = resultado - teste_marcacoes

acertos = [d for d in diferencas if d == 0]
total_de_acertos = len(acertos)
total_de_elementos = len(teste_dados)

taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

print("com base nos dados {0:.2f}, realizariam as compras no site".format(taxa_de_acerto))
