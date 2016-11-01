#!/usr/bin/python

import csv
import math
import numpy as np
from numpy import linalg as LA
from sklearn import svm
from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report as cr


def loadCsv(filename):
    lines = csv.reader(open(filename, 'rb'))
    dataset = list(lines)
    new=[]
    count = 0
    for i in range(0,len(dataset)):
        flag = 0
        for j in range(len(dataset[i])):
            if dataset[i][j] == '':
                flag=1
            else:
                count=count+1
                dataset[i][j]=float(dataset[i][j])
                dataset[i][j] = int(math.floor(dataset[i][j]))
        if flag==0:
            new.append(dataset[i])
    return new

def train(dataset,label):
    clf=svm.SVC()
    clf.fit(dataset,label)
    return clf

def predict(model, vector):
    return model.predict(vector)

def classify(model, featureVectors):
    true = 0
    total = 0
    z = []
    featureVectors=np.array(featureVectors)
    print featureVectors[:-1]
    for feature in featureVectors:
        if feature[-1] == predict(model, feature[:-1]):
            true += 1
        total += 1
	if(total%10000==0):
	    print total/10000
    print "Accuracy : ",
    print (true * 100) / total


def clusterise(dataset):
    separated={}
    for i in range(len(dataset)):
        if(dataset[i][-1] not in separated):
            separated[dataset[i][-1]]=[]
        separated[dataset[i][-1]].append(dataset[i])
    return separated


def main():
   # csvFiles = glob.glob(path + "/*.csv")
    filename = 'final.csv'
    dataset = loadCsv(filename)
    cluster_class=clusterise(dataset)
    train_data=[]
#    for i in range(len(cluster_class)):
#        print len(cluster_class[i]),
    for i in range(0,2000):
        for j in range(len(cluster_class)):
            train_data.append(cluster_class[j][i])
#            print j,i,
    print len(train_data)
    print len(train_data[1])
    train_label=[]
    print 'Label Extraction'
    for i in range(len(train_data)):
        train_label.append(train_data[i][-1])
    train_data=np.matrix(train_data)
    print train_data.shape[0],train_data.shape[1]
    train_data=np.delete(train_data,train_data.shape[1]-1,1)
    print 'Loaded data file {0} with {1} rows'.format(filename,len(dataset))
    print train_data.shape[0],train_data.shape[1]
    print 'Training Model'
    model=train(train_data,train_label)
    print 'Model Published'
    dataset=np.mat(dataset)
    classify(model,dataset)

main()
