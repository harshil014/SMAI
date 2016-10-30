#!/usr/bin/python

import csv
import math


def loadCsv(filename):
    lines = csv.reader(open(filename, 'rb'))
    dataset = list(lines)
    count = 0
    csvfile = open('2.csv', 'w')
    write = csv.writer(csvfile, delimiter=',')
    for i in range(len(dataset)):
        flag = 0
        mn=0.0
        ct=0
        for j in range(len(dataset[i])):
            if dataset[i][j] == '':
                ct+=1
                dataset[i][j] = -1
            else:
                dataset[i][j] = int(math.floor(float(dataset[i][j])))
                mn+=dataset[i][j]
        mn=mn/(len(dataset[i])-ct)
        for j in range(len(dataset[i])):
            if dataset[i][j] == -1:
                dataset[i][j] = mn
    write.writerow(dataset[i])
    with open(filename) as f:
        z = csv.reader(f, delimiter='\t')
    return dataset


def separateByCluster(dataset):
    separated = {}
    for i in range(len(dataset)):
        vector = dataset[i]
        if vector[-1] not in separated:
            separated[vector[-1]] = []
        separated[vector[-1]].append(vector)
    return separated

def calculate_prior(cluster_data,k):
    temp=[]
    for i in range(len(cluster_data)):
        print len(cluster_data[i]),
        #f=float(len(cluster_data[0]))
        temp.append(len(cluster_data[i]))
    return temp

def calc_mean(data):
    k=len(data);
    sum=0
    for i in range(len(data)):
        sum+=data[i]
    temp_sum=float(sum)
    temp_sum=temp_sum/k
    return temp_sum

def calc_stdev(data):
    temp_mean = calc_mean(data)
    sum=0
    k=len(data)
    for i in range(len(data)):
        sum+=(data[i]-temp_mean)*(data[i]-temp_mean)
    temp_sum=float(sum)
    temp_sum=temp_sum/k
    return temp_sum    

def normalise_data(cluster_data,meanx,stdevx):
	part3=[]
	for i in range(len(cluster_data)):
		part2=[]
		for j in range(len(cluster_data[i])):
			part1=[]
			for k in range(0,len(cluster_data[i][j])):
				temp = (cluster_data[i][j][k]-meanx[i][j])*(cluster_data[i][j][k]-meanx[i][j]);
				temp = temp/(stdevx[i][j]*stdevx[i][j])
				r=1/math.sqrt(2*math.pi*(stdevx[i][j]))
				temp = temp+ math.log(r,math.exp(1))
				part1.append(temp);
			part2.append(part1);
		part3.append(part2);
	return part3



def seperate_cluster(dataset):
    vec=[]
    for i in range(0,10000):
        temp=dataset[i][-1]
        vec.append(temp)
    return vec

def validate_cluster(meanx,varx,dataset,prior):
    answers=[]
    for i in range(0,10000):
        temp_vec=dataset[i]
        cluster=naive_bayes(meanx,varx,temp_vec,prior)
        answers.append(cluster)
    return answers


def naive_bayes(meanx,varx,ip_vec,prior):
    max_prob=-100000000000
    max_cluster=-1
    for i in range(len(prior)): # for all cluster have to check prob
        curr_prob=0
        for j in range(len(ip_vec)-1):
            temp=(ip_vec[j]-meanx[i][j])
            temp=float(temp*temp)
            temp=temp/(2*varx[i][j])
            curr_prob+=(-1*temp)
        curr_prob+=math.log(prior[i],math.exp(1))
        if curr_prob > max_prob:
            max_prob=curr_prob
            max_cluster=i
    return max_cluster

def accuracy(ground_truth,observed_clusters):
    count=0
    for i in range(0,10000):
        if ground_truth[i]==observed_clusters[i]:
            count=count+1
    ans= float(count)
    response=ans/10001
    return response*100



def main():
    filename = 'ab.csv'
    dataset = loadCsv(filename)
    print 'Loaded data file {0} with {1} rows'.format(filename,len(dataset))
    
    #Data Clusering on the basis of the last column entries
    print 'Data Clustering '

    cluster_data = separateByCluster(dataset)
    print len(cluster_data)


    #Prior Probability Calculation
    print 'Prior Probability Calculation'
    prior =  calculate_prior(cluster_data,len(dataset))
    print prior[0]

    #Mean and Standard Deviation Calculation Cluster Wise
    print 'Mean and Standard Deviation Calculation'
    meanx=[]
    stdevx=[]
       # meanx is the vector with individual cluster means of the features for the respective cluster
    # stdevx is the vector with individual cluster standard deviations of the features for the respective cluster
    
    for i in range(len(cluster_data)):
        new1=[]
        new2=[]
        for j in range(len(cluster_data[i])):
            new1.append(calc_mean(cluster_data[i][j]))
            new2.append(calc_stdev(cluster_data[i][j]))
        meanx.append(new1)
        stdevx.append(new2)
        
    #print 'Normalising Content'
    #normalized=normalise_data(cluster_data,meanx,stdevx)
    print prior,
    observed_clusters=validate_cluster(meanx,stdevx,dataset,prior)
    print observed_clusters,
    ground_truth=seperate_cluster(dataset)
    print ground_truth,
    percentage=accuracy(ground_truth,observed_clusters)
    print percentage
    print 'Done'
    
main()
