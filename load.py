#!/usr/bin/python
# -*- coding: utf-8 -*-

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
        for j in range(len(dataset[i])):
            if dataset[i][j] == '':
                dataset[i][j] = 0
            else:
                dataset[i][j] = int(math.floor(float(dataset[i][j])))
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
        f=float(len(cluster_data[0]))
        temp.append(f/k)
    return temp

def main():
    filename = 'ab.csv'
    dataset = loadCsv(filename)
    print 'Loaded data file {0} with {1} rows'.format(filename,len(dataset))
    print 'Data Clustering '
    cluster_data = separateByCluster(dataset)
    print len(cluster_data)
    print 'Prior Probability Calculation'
    prior =  calculate_prior(cluster_data,len(dataset))
    print prior[0]

main()


            