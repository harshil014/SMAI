#!/usr/bin/python
# -*- coding: utf-8 -*-
#Naive Bayes Algorithm Implemented
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
   # print data.shape
    sum1=np.zeros(shape=(1,data.shape[1]))
   # print sum1[0,:].shape
   # print data[0,:].shape
    for i in range(len(data)):
        sum1[0,:]=sum1[0,:]+data[i,:]
    temp_sum=sum1.astype(np.float)
    temp_sum=temp_sum/k
    return temp_sum
def calc_mean1(data):
    k=len(data)
    #print data.shape
    data=np.array(data)
    data=data.astype(np.float)
   # print data.shape
    sum1=np.zeros(shape=(1,data.shape[1]))
   # print sum1[0,:].shape
   # print data[0,:].shape
    for i in range(len(data)):
        sum1[0,:]=sum1[0,:]+data[i,:]
    temp_sum=sum1.astype(np.float)
    temp_sum=temp_sum/k
    return temp_sum
def calc_stdev1(data):
    data=np.array(data)
    data=data.astype(np.float)
    temp_mean = calc_mean1(data)
    sum1=np.zeros(shape=(1,data.shape[1]))
    k=len(data)
    for i in range(len(data)):
        sum1[0,:]=((data[i,:]-temp_mean)*(data[i,:]-temp_mean))+sum1[0,:]
    temp_sum=sum1.astype(np.float)
    temp_sum=temp_sum/k
    return temp_sum
def calc_stdev(data):
    data=np.array(data)
    data=data.astype(np.float)
    temp_mean = calc_mean(data)
    sum1=np.zeros(shape=(1,data.shape[1]))
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
        if (stdevx[0,i]!=0):
            cluster_data[:,i]=cluster_data[:,i]/stdevx[0,i]
    return cluster_data

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
    #print v[:,0]
    print 'ann'
    print v.shape
    #print v[0][0]
    #a=np.zeros(shape=(len(v),kn),dtype=object)
    #a=np.mat(a)
    #v=np.mat(v)
    #for i in range(len(v)):
    #    for j in range(0,kn):
    #        a[i][j]=v[i][j]
    a=np.zeros(shape=(len(v),len(v)))
    a=v;
    for i in range(0,len(v)-kn):
        a=np.delete(a, a.shape[1]-1, 1)
    #print a.shape
    #print 'Done'
    a=np.array(a);
    #print a.shape
    #print nor_data.shape
    new_data = np.zeros(shape=(len(dataset),kn))
    new_data = np.mat(nor_data) * np.mat(a)
    return new_data
def calculate_prior(cluster_data,k):
    temp=[]
    max1=0
    #print len(cluster_data)
    for i in range(len(cluster_data)):
        #print len(cluster_data[i]), i,
        f=float(len(cluster_data[i]))
        temp.append(f/k)
    return temp

def separateByCluster(dataset,label):
    print len(dataset)
    print len(label)
    separated = []
    for i in range(0,100):
        separated.append([])
    for i in range(len(dataset)):
        vector = dataset[i]
        separated[label[i]].append(vector)
        #for j in 

    return separated

def seperate_cluster(dataset):
    vec=[]
    for i in range(len(dataset)):
        #print dataset[i][-1]
        temp=int(math.floor(float(dataset[i][-1])))
        vec.append(temp)
    return vec

def naive_bayes(meanx,varx,ip_vec,prior):
    max_prob=-10000000000000
    max_cluster=-1
    ip_vec=np.array(ip_vec)
   # print ip_vec.shape
    #print varx[0][0]
    #print ip_vec
   # print len(prior)
    for i in range(len(prior)): # for all cluster have to check prob
        curr_prob=0
        for j in range(ip_vec.shape[1]):
            #print meanx[i]
            temp=(ip_vec[0][j]-meanx[i][0][j])
            #print temp,'temp'
            temp=float(temp*temp)
            temp=temp/(2*varx[i][0][j])
            curr_prob+=(-1*temp)
        curr_prob+=math.log(prior[i],math.exp(1))
        if curr_prob > max_prob:
            max_prob=curr_prob
            max_cluster=i
    return max_cluster
def validate_cluster(meanx,varx,dataset,prior):
    print 'validate start'
    answers=[]
    for i in range(10000):
        temp_vec=dataset[i]
        cluster=naive_bayes(meanx,varx,temp_vec,prior)
        answers.append(cluster)
    print 'validate end'
    return answers
def accuracy(ground_truth,observed_clusters):
    count=0
    for i in range(len(observed_clusters)):
        if ground_truth[i]==observed_clusters[i]:
            count=count+1
    ans= float(count)
    response=ans/len(ground_truth)
    print 'correct'
    print ans
    return response*100

def main():
    filename = 'final.csv'
    dataset = loadCsv(filename)
    print 'Loaded data file {0} with {1} rows'.format(filename,len(dataset))
    
    #Data Clusering on the basis of the last column entries
    print 'Data Clustering '

   # cluster_data = separateByCluster(dataset)
    kn=12
    dataset=np.array(dataset)
    label=seperate_cluster(dataset)
    #print label
    print len(dataset)
    print len(dataset[0])
    dataset=np.array(dataset)
    dataset=np.delete(dataset, len(dataset[1])-1, 1)
    new_data=np.zeros(shape=(len(dataset),kn))   
    new_data=pca(dataset,kn)
    print len(new_data)
    print len(new_data[1])
    print 'PCA done'
    cluster_data = separateByCluster(new_data,label)
    print 'Clustering done'
   # print cluster_data[1][1]
    #Prior Probability Calculation
    #cluster_data=np.array(cluster_data)
    prior=calculate_prior(cluster_data,len(dataset))
    print 'prior calculated'
    print prior,
    print 'Mean and Standard Deviation Calculation'
    #print (np.matrix(cluster_data[0]).shape)
    meanx=[]
    stdevx=[]
    for i in range(len(cluster_data)):
        an=np.zeros(shape=(len(cluster_data[i]),len(cluster_data[i][0].T)))
        for j in range(len(cluster_data[i])):
            an[j,:]=cluster_data[i][j]
        #print an.shape
        meanx.append(calc_mean1(an))
        stdevx.append(calc_stdev1(an))
    #print meanx
   # print len(cluster_data)
   # print cluster_data[1]
   # for i in range(1,len(cluster_data)):
   #     print len(cluster_data[i]),
    print len(new_data)
    #print prior,
    observed_clusters=validate_cluster(meanx,stdevx,new_data,prior)
    #print observed_clusters,
    #ground_truth=seperate_cluster(dataset)
    #print ground_truth,
    percentage=accuracy(label,observed_clusters)
    print percentage
    print 'Done'
    
    
main()