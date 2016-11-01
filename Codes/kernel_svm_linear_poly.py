import numpy as np
from sklearn import svm, datasets

data = np.genfromtxt('final1.csv', delimiter=',')
labels = data[:,(len(data[0])-1)]
data = np.delete(data,-1,1)
print len(labels), len(data)
clf = svm.SVC(kernel='poly')
clf.fit(data,labels)

new_labels = []

for i in range(len(data)):
    new_labels.append(clf.predict(data[i]))

print new_labels == labels




