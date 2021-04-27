#AUTOR: Dagberto Rigue

import pandas as pd
import numpy as np
from sklearn import datasets, svm, metrics, model_selection
import pickle
#from vetor_treinamento import targetTraining

#Classificador do SVM
classifier = svm.SVC(gamma=0.001)


##### IMPORTACAO DOS DADOS PARA TREINAMENTO
#faz a leitura do arquivo txt separando cada elemento ao identificar uma virgula.
file1 = 'vetor01_normal.txt'
data1 = open(file1, 'rt')
normal_vector1 = np.loadtxt(data1, delimiter=",")

file2 = 'vetor02_normal.txt'
data2 = open(file2, 'rt')
normal_vector2 = np.loadtxt(data2, delimiter=",")

file3 = 'vetor03_normal.txt'
data3 = open(file3, 'rt')
normal_vector3 = np.loadtxt(data3, delimiter=",")

file4 = 'vetor04_normal.txt'
data4 = open(file4, 'rt')
normal_vector4 = np.loadtxt(data4, delimiter=",")

file5 = 'vetor05_normal.txt'
data5 = open(file5, 'rt')
normal_vector5 = np.loadtxt(data5, delimiter=",")

file6 = 'vetor06_normal.txt'
data6 = open(file6, 'rt')
normal_vector6 = np.loadtxt(data6, delimiter=",")

file7 = 'vetor07_normal.txt'
data7 = open(file7, 'rt')
normal_vector7 = np.loadtxt(data7, delimiter=",")

file8 = 'vetor08_normal.txt'
data8 = open(file8, 'rt')
normal_vector8 = np.loadtxt(data8, delimiter=",")

file9 = 'vetor09_normal.txt'
data9 = open(file9, 'rt')
normal_vector9 = np.loadtxt(data9, delimiter=",")

file10 = 'vetor10_normal.txt'
data10 = open(file10, 'rt')
normal_vector10 = np.loadtxt(data10, delimiter=",")

file11 = 'vetor11_normal.txt'
data11 = open(file11, 'rt')
normal_vector11 = np.loadtxt(data11, delimiter=",")

file12 = 'vetor12_normal.txt'
data12 = open(file12, 'rt')
normal_vector12 = np.loadtxt(data12, delimiter=",")

file13 = 'vetor13_normal.txt'
data13 = open(file13, 'rt')
normal_vector13 = np.loadtxt(data13, delimiter=",")

file14 = 'vetor14_normal.txt'
data14 = open(file14, 'rt')
normal_vector14 = np.loadtxt(data14, delimiter=",")

file15 = 'vetor15_normal.txt'
data15 = open(file15, 'rt')
normal_vector15 = np.loadtxt(data15, delimiter=",")

file16 = 'vetor16_normal.txt'
data16 = open(file16, 'rt')
normal_vector16 = np.loadtxt(data16, delimiter=",")

file17 = 'vetor17_normal.txt'
data17 = open(file17, 'rt')
normal_vector17 = np.loadtxt(data17, delimiter=",")

file18 = 'vetor18_normal.txt'
data18 = open(file18, 'rt')
normal_vector18 = np.loadtxt(data18, delimiter=",")

file19 = 'vetor19_normal.txt'
data19 = open(file19, 'rt')
normal_vector19 = np.loadtxt(data19, delimiter=",")

file20 = 'vetor20_normal.txt'
data20 = open(file20, 'rt')
normal_vector20 = np.loadtxt(data20, delimiter=",")

file21 = 'vetor21_alarme.txt'
data21 = open(file20, 'rt')
alarm_vector21 = np.loadtxt(data21, delimiter=",")

file22 = 'vetor22_alarme.txt'
data22 = open(file22, 'rt')
alarm_vector22 = np.loadtxt(data22, delimiter=",")

file23 = 'vetor23_alarme.txt'
data23 = open(file23, 'rt')
alarm_vector23 = np.loadtxt(data23, delimiter=",")

file24 = 'vetor24_alarme.txt'
data24 = open(file24, 'rt')
alarm_vector24 = np.loadtxt(data24, delimiter=",")

file25 = 'vetor25_alarme.txt'
data25 = open(file25, 'rt')
alarm_vector25 = np.loadtxt(data25, delimiter=",")

file26 = 'vetor26_alarme.txt'
data26 = open(file26, 'rt')
alarm_vector26 = np.loadtxt(data26, delimiter=",")

file27 = 'vetor27_alarme.txt'
data27 = open(file27, 'rt')
alarm_vector27 = np.loadtxt(data27, delimiter=",")

file28 = 'vetor28_alarme.txt'
data28 = open(file28, 'rt')
alarm_vector28 = np.loadtxt(data28, delimiter=",")

file29 = 'vetor29_alarme.txt'
data29 = open(file29, 'rt')
alarm_vector29 = np.loadtxt(data29, delimiter=",")

file30 = 'vetor30_alarme.txt'
data30 = open(file30, 'rt')
alarm_vector30 = np.loadtxt(data30, delimiter=",")

file31 = 'vetor31_alarme.txt'
data31 = open(file31, 'rt')
alarm_vector31 = np.loadtxt(data31, delimiter=",")

file32 = 'vetor32_alarme.txt'
data32 = open(file32, 'rt')
alarm_vector32 = np.loadtxt(data32, delimiter=",")

file33 = 'vetor33_alarme.txt'
data33 = open(file33, 'rt')
alarm_vector33 = np.loadtxt(data33, delimiter=",")

file34 = 'vetor34_alarme.txt'
data34 = open(file34, 'rt')
alarm_vector34 = np.loadtxt(data34, delimiter=",")

file35 = 'vetor35_alarme.txt'
data35 = open(file35, 'rt')
alarm_vector35 = np.loadtxt(data35, delimiter=",")

file36 = 'vetor36_alarme.txt'
data36 = open(file36, 'rt')
alarm_vector36 = np.loadtxt(data36, delimiter=",")

file37 = 'vetor37_alarme.txt'
data37 = open(file37, 'rt')
alarm_vector37 = np.loadtxt(data37, delimiter=",")

file38 = 'vetor38_alarme.txt'
data38 = open(file38, 'rt')
alarm_vector38 = np.loadtxt(data38, delimiter=",")

file39 = 'vetor39_alarme.txt'
data39 = open(file39, 'rt')
alarm_vector39 = np.loadtxt(data39, delimiter=",")

file40 = 'vetor40_alarme.txt'
data40 = open(file40, 'rt')
alarm_vector40 = np.loadtxt(data40, delimiter=",")

file41 = 'vetor41_critico.txt'
data41 = open(file41, 'rt')
critical_vector41 = np.loadtxt(data41, delimiter=",")

file42 = 'vetor42_critico.txt'
data42 = open(file42, 'rt')
critical_vector42 = np.loadtxt(data42, delimiter=",")

file43 = 'vetor43_critico.txt'
data43 = open(file43, 'rt')
critical_vector43 = np.loadtxt(data43, delimiter=",")

file44 = 'vetor44_critico.txt'
data44 = open(file44, 'rt')
critical_vector44 = np.loadtxt(data44, delimiter=",")

file45 = 'vetor45_critico.txt'
data45 = open(file45, 'rt')
critical_vector45 = np.loadtxt(data45, delimiter=",")

file46 = 'vetor46_critico.txt'
data46 = open(file46, 'rt')
critical_vector46 = np.loadtxt(data46, delimiter=",")

file47 = 'vetor47_critico.txt'
data47 = open(file47, 'rt')
critical_vector47 = np.loadtxt(data47, delimiter=",")

file48 = 'vetor48_critico.txt'
data48 = open(file48, 'rt')
critical_vector48 = np.loadtxt(data48, delimiter=",")

file49 = 'vetor49_critico.txt'
data49 = open(file49, 'rt')
critical_vector49 = np.loadtxt(data49, delimiter=",")

file50 = 'vetor50_critico.txt'
data50 = open(file50, 'rt')
critical_vector50 = np.loadtxt(data50, delimiter=",")

file51 = 'vetor51_critico.txt'
data51 = open(file51, 'rt')
critical_vector51 = np.loadtxt(data51, delimiter=",")

file52 = 'vetor52_critico.txt'
data52 = open(file52, 'rt')
critical_vector52 = np.loadtxt(data52, delimiter=",")

file53 = 'vetor53_critico.txt'
data53 = open(file53, 'rt')
critical_vector53 = np.loadtxt(data53, delimiter=",")

file54 = 'vetor54_critico.txt'
data54 = open(file54, 'rt')
critical_vector54 = np.loadtxt(data54, delimiter=",")

file55 = 'vetor55_critico.txt'
data55 = open(file55, 'rt')
critical_vector55 = np.loadtxt(data55, delimiter=",")

file56 = 'vetor56_critico.txt'
data56 = open(file56, 'rt')
critical_vector56 = np.loadtxt(data56, delimiter=",")

file57 = 'vetor57_critico.txt'
data57 = open(file57, 'rt')
critical_vector57 = np.loadtxt(data57, delimiter=",")

file58 = 'vetor58_critico.txt'
data58 = open(file58, 'rt')
critical_vector58 = np.loadtxt(data58, delimiter=",")

file59 = 'vetor59_critico.txt'
data59 = open(file59, 'rt')
critical_vector59 = np.loadtxt(data59, delimiter=",")

file60 = 'vetor60_critico.txt'
data60 = open(file60, 'rt')
critical_vector60 = np.loadtxt(data60, delimiter=",")


#REALIZA O TREINAMENTO DO SCRIPT
#samples = [alarm_vector21, critical_vector41]

#REALIZA O TREINAMENTO DO SCRIPT
samples = [normal_vector1, normal_vector2, normal_vector3, normal_vector4, normal_vector5, normal_vector6, normal_vector7, normal_vector8, normal_vector9, normal_vector10,
           normal_vector11, normal_vector12, normal_vector13, normal_vector14, normal_vector15, normal_vector16, normal_vector17, normal_vector18, normal_vector19, normal_vector20,
           alarm_vector21, alarm_vector22, alarm_vector23, alarm_vector24, alarm_vector25, alarm_vector26, alarm_vector27, alarm_vector28, alarm_vector29, alarm_vector30,
           alarm_vector31, alarm_vector32, alarm_vector33, alarm_vector34, alarm_vector35, alarm_vector36, alarm_vector37, alarm_vector38, alarm_vector39, alarm_vector40,
           critical_vector41, critical_vector42, critical_vector43, critical_vector44, critical_vector45, critical_vector46, critical_vector47, critical_vector48, critical_vector49,
           critical_vector50, critical_vector51, critical_vector52, critical_vector53, critical_vector54, critical_vector55, critical_vector56, critical_vector57, critical_vector58,
           critical_vector59, critical_vector60]

targetTraining = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                  2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                  3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]

#print("Vetor utilizado para o treinamento")
#print(samples)
#print(targetTraining)

classifier.fit(samples, targetTraining)


#salva o arquivo no diretorio do projeto
saveFile = 'teste_svm_treinado_teste_4.sav'
pickle.dump(classifier, open(saveFile, 'wb'))

