# Author: Dagberto Rigue


# Script usado para classificar o status de uma amostra coletada em campo.
# O nome do arquivo que sera carregado pelo script deve ser passado como parametro ao executar o script pelo cmd

# Exemplo:
# No cmd do windows
# C:\Users\administrator.AUTOMATIONPR\PycharmProjects\script_classificador_teste_3  python script_classificador_teste_3.py Vetor1_normal.csv


#resultado da classificacao
# 1 normal
# 2 alarme
# 3 critico

import pandas as pd
import numpy as np
from sklearn import datasets, svm, metrics, model_selection
import pickle
import sys

##### IMPORTACAO DOS DADOS
#faz a leitura do arquivo csv separando cada elemento ao identificar uma virgula
#dados referentes a uma amostra classificada como normal


#le o nome do arquivo informado pelo usuario
for aux in sys.argv:
    file = aux

data = open(file, 'rt')
vector = np.loadtxt(data, delimiter=",")

#carrega o script treinado
fileTrained = pickle.load(open('teste_svm_treinado_teste_2.sav', 'rb'))
classifier = fileTrained
print(fileTrained)

# CLASSIFICACAO
dataTest = [vector]
targetTest = [1]

test = classifier.predict(dataTest)

print("Classification report for classifier %s:\n%s\n"
      % (classifier, metrics.classification_report(targetTest, test)))
print("Confusion matrix:\n%s" % metrics.confusion_matrix(targetTest, test))

