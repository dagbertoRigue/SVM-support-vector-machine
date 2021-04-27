#Author: Dagberto Rigue


#Script usado para classificar o status de uma amostra coletada em campo

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

#arquivo = raw_input("Digite o nome do arquivo: ")
#Author: Dagberto Rigue


#Script usado para classificar o status de uma amostra coletada em campo

#resultado da classificacao
# 1 normal
# 2 alarme
# 3 critico

import pandas as pd
import numpy as np
from sklearn import datasets, svm, metrics, model_selection
import pickle

##### IMPORTACAO DOS DADOS
#faz a leitura do arquivo csv separando cada elemento ao identificar uma virgula
#dados referentes a uma amostra classificada como normal
file1 = 'Vetor 1_normal.csv'
data1 = open(file1, 'rt')
vetorNormal1 = np.loadtxt(data1, delimiter=",")

file2 = 'Vetor 2_normal.csv'
data2 = open(file2, 'rt')
vetorNormal2 = np.loadtxt(data2, delimiter=",")

file3 = 'Vetor 3_normal.csv'
data3 = open(file3, 'rt')
vetorNormal3 = np.loadtxt(data3, delimiter=",")

file4 = 'Vetor 4_alarme.csv'
data4 = open(file4, 'rt')
vetorAlarme1 = np.loadtxt(data4, delimiter=",")

file5 = 'Vetor 5_alarme.csv'
data5 = open(file5, 'rt')
vetorAlarme2 = np.loadtxt(data5, delimiter=",")

file6 = 'Vetor 6_critico.csv'
data6 = open(file6, 'rt')
vetorCritico1 = np.loadtxt(data6, delimiter=",")

file7 = 'Vetor 7_alarme.csv'
data7 = open(file7, 'rt')
vetorAlarme3 = np.loadtxt(data7, delimiter=",")

file8 = 'Vetor 8_normal.csv'
data8 = open(file8, 'rt')
vetorNormal8 = np.loadtxt(data8, delimiter=",")

file9 = 'Vetor 9_normal.csv'
data9 = open(file9, 'rt')
vetorNormal9 = np.loadtxt(data9, delimiter=",")

file10 = 'Vetor 10_normal.csv'
data10 = open(file10, 'rt')
vetorNormal10 = np.loadtxt(data10, delimiter=",")

file11 = 'Vetor 11_normal.csv'
data11 = open(file11, 'rt')
vetorNormal11 = np.loadtxt(data11, delimiter=",")

file12 = 'Vetor 12_normal.csv'
data12 = open(file12, 'rt')
vetorNormal12 = np.loadtxt(data12, delimiter=",")

file13 = 'Vetor 13_normal.csv'
data13 = open(file13, 'rt')
vetorNormal13 = np.loadtxt(data13, delimiter=",")

file14 = 'Vetor 14_normal.csv'
data14 = open(file14, 'rt')
vetorNormal14 = np.loadtxt(data14, delimiter=",")

file15 = 'Vetor 15_normal.csv'
data15 = open(file15, 'rt')
vetorNormal15 = np.loadtxt(data15, delimiter=",")


#carrega o script treinado
file = pickle.load(open('teste_svm_treinado_teste_2.sav', 'rb'))
classifier = file
print(file)

# CLASSIFICACAO
dataTest = [vetorNormal1, vetorNormal2, vetorNormal3, vetorAlarme1, vetorAlarme2, vetorCritico1, vetorAlarme3, vetorNormal8, vetorNormal9,
           vetorNormal10, vetorNormal11, vetorNormal12, vetorNormal13, vetorNormal14, vetorNormal15]

targetTest = [1, 1, 1, 2, 2, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1]

test = classifier.predict(dataTest)

print("Classification report for classifier %s:\n%s\n"
      % (classifier, metrics.classification_report(targetTest, test)))
print("Confusion matrix:\n%s" % metrics.confusion_matrix(targetTest, test))


for sis in sys.argv:
    arquivo = sis


file1 = arquivo
data1 = open(file1, 'rt')
vetorNormal1 = np.loadtxt(data1, delimiter=",")

#carrega o script treinado
file = pickle.load(open('teste_svm_treinado_teste_2.sav', 'rb'))
classifier = file
print(file)

# CLASSIFICACAO
dataTest = [vetorNormal1]

targetTest = [1]

test = classifier.predict(dataTest)

print("Classification report for classifier %s:\n%s\n"
      % (classifier, metrics.classification_report(targetTest, test)))
print("Confusion matrix:\n%s" % metrics.confusion_matrix(targetTest, test))

