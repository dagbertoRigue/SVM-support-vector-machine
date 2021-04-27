
#Script responsavel por ler os dados de um arquivo txt
#e imprimi-los na tela
file = open('/dagbertoRigue/svm/Vetor 1_normal.csv', 'r')
text = file.read()
print(text)
file.close()