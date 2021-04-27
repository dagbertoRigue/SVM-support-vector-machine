
import numpy as np
import pickle
import scipy
import skimage
import matplotlib
from sklearn import metrics
from sklearn.metrics import precision_recall_fscore_support
import sys


#Script responsavel por ler os dados de um arquivo txt
#e imprimi-los na tela
file = open('/dagbertoRigue/svm/Vetor 1_normal.csv', 'r')
text = file.read()
print(sys.path)
#print(text)
file.close()