
print(__doc__)


# Standard scientific Python imports
import matplotlib as plt
import numpy as np
import pandas as pd

# Import datasets, classifiers and performance metrics
from sklearn import datasets, svm, metrics

# The digits dataset
digits = datasets.load_digits()




# Create a classifier: a support vector classifier
classifier = svm.SVC(gamma=0.001)

#importando o arquivo csv
#with open('teste_svm.csv', 'r') as f:
#      treino = f.readlines()
#print(treino)
#######



##### MEU EXEMPLO #####
# TREINO
samples = [[1, 2, 3],[2, 2, 2],[3, 3, 3],[4, 4, 4]]
target = [1, 2, 3, 4]
print(samples)
print(target)
classifier.fit(samples, target)

# CLASSIFICACAO
dataTest = [[1, 2, 3],[2, 2, 2],[3, 2, 3],[4, 4, 4]]
targetTest = [1, 2, 3, 4]
test = classifier.predict(dataTest)

print("Classification report for classifier %s:\n%s\n"
      % (classifier, metrics.classification_report(targetTest, test)))
print("Confusion matrix:\n%s" % metrics.confusion_matrix(targetTest, test))
##### MEU EXEMPLO #####
