#!/usr/bin/python
#PCA Code

import csv
import math
import numpy as np
from numpy import linalg as LA
from sklearn.svm import SVC

def loadCsv(filename):
    lines = csv.reader(open(filename, 'rb'))
    dataset = list(lines)
    new=[]
    count = 0
    for i in range(len(dataset)):
        flag = 0
        for j in range(len(dataset[i])):
            if dataset[i][j] == '':
                flag=1
            else:
                count=count+1
                dataset[i][j] = dataset[i][j]
        if flag==0:
            new.append(dataset[i])
    return np.matrix(new)
def calc_mean(data):
    k=len(data)
    data=np.array(data)
    data=data.astype(np.float)
    sum1=np.zeros(shape=(1,len(data[1])))
    for i in range(len(data)):
        sum1[0,:]=sum1[0,:]+data[i,:]
    temp_sum=sum1.astype(np.float)
    temp_sum=temp_sum/k
    return temp_sum

def calc_stdev(data):
    data=np.array(data)
    data=data.astype(np.float)
    temp_mean = calc_mean(data)
    sum1=np.zeros(shape=(1,len(data[1])))
    k=len(data)
    for i in range(len(data)):
        sum1[0,:]=((data[i,:]-temp_mean)*(data[i,:]-temp_mean))+sum1[0,:]
    temp_sum=sum1.astype(np.float)
    temp_sum=temp_sum/k
    return temp_sum    

def normalise_data(cluster_data,meanx,stdevx):
    cluster_data=np.array(cluster_data)
    cluster_data=cluster_data.astype(np.float)
    meanx=np.array(meanx)
    meanx=meanx.astype(np.float)
    stdevx=np.array(stdevx)
    stdevx=stdevx.astype(np.float)
    for i in range(len(cluster_data[0])):
        cluster_data[:,i]-=meanx[0,i]
        cluster_data[:,i]=cluster_data[:,i]/stdevx[0,i]
    return cluster_data
def kernel_pca(dataset):
    gama=0.0000001;
    kn=10
    K= np.zeros(shape=(len(dataset),len(dataset)))
    for i in range(len(dataset)):
        for j in range(len(dataset)):
            x = dataset[i] - dataset[j]
            K[i][j] = math.exp(-gamma * LA.norm(x))
    one = np.full((100,100), 1/len(dataset))
    K_tilde = np.zeros(shape=(100,100))
    K_tilde = K - one*K - K*one + one*K*one
    w, v = LA.eig(K_tilde)
    a=np.zeros(shape=(len(v),kn))
    for i in range(0,kn):
        a[:,i]=(v[:,i])
    new_data = np.zeros(shape=(len(dataset),kn))
    new_data = np.mat(K_tilde) * np.mat(a.T)
    return new_data
def pca(dataset,kn):
    meanx=calc_mean(dataset)
    stdevx=calc_stdev(dataset)
    nor_data=normalise_data(dataset,meanx,stdevx)
    nor_data=np.mat(nor_data)
    # scatter matrix
    sc_mat=nor_data.transpose()*nor_data;
    sc_mat=sc_mat.astype(np.float)
    sc_mat=sc_mat/len(dataset)
    w, v = LA.eig(sc_mat)
    print 'ann'
    print len(v)
    a=[]
    for i in range(0,kn):
        a.append(v[:,i].T)
    print 'Done'
    a=np.array(a);
    a=a.T
    new_data = np.zeros(shape=(len(dataset),kn))
    new_data = np.mat(nor_data) * np.mat(a)
    return new_data
def seperate_cluster(dataset):
    vec=[]
    for i in range(0,10000):
        temp=dataset[i][-1]
        vec.append(temp)
    return vec		

def main():
   # csvFiles = glob.glob(path + "/*.csv")
    filename = 'ab.csv'
    dataset = loadCsv(filename)
    print 'Loaded data file {0} with {1} rows'.format(filename,len(dataset))
    
    #Data Clusering on the basis of the last column entries
    print 'Data Clustering '

   # cluster_data = separateByCluster(dataset)
    kn=10
    new_data=np.zeros(shape=(len(dataset),kn))   
    new_data=pca(dataset,kn)
   # print len(cluster_data)
   # print cluster_data[1]
   # for i in range(1,len(cluster_data)):
   #     print len(cluster_data[i]),
    print len(new_data)

main()