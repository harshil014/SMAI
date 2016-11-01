#!/usr/bin/python
# -*- coding: utf-8 -*-
# Cluster Separation
import csv
import math

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
    return new


def separateByCluster(dataset):
    separated = {}
    for i in range(1,len(dataset)):
        vector = dataset[i]
        if int(vector[-1]) not in separated:
            separated[int(vector[-1])] = []
        separated[int(vector[-1])].append(vector)
 #   print separated[1]
    return separated


def main():
    filename = ['split_ac.csv','split_ad.csv','split_ae.csv','split_af.csv','split_ag.csv','split_ah.csv','split_ai.csv','split_aj.csv','split_ak.csv','split_al.csv','split_am.csv','split_an.csv','split_ao.csv','split_ap.csv','split_aq.csv','split_ar.csv','split_as.csv','split_at.csv','split_au.csv','split_av.csv','split_aw.csv','split_ax.csv','split_ay.csv','split_az.csv','split_ba.csv','split_bb.csv','split_bd.csv','split_be.csv','split_bf.csv','split_bg.csv','split_bh.csv','split_bi.csv','split_bj.csv','split_bk.csv','split_bl.csv']
    print filename[1]
    sum=[]
    for j in range(0,100):
        sum.append(0);
    print len(sum)

    for i in range(len(filename)):
        dataset = loadCsv(filename[i])
        print 'Loaded data file {0} with {1} rows'.format(filename[i],len(dataset))
    
    #Data Clusering on the basis of the last column entries
        print 'Data Clustering '

        cluster_data = separateByCluster(dataset)
        print len(cluster_data)
 #   print cluster_data[1]
        for j in range(len(cluster_data)):
            sum[j]=sum[j]+len(cluster_data[j])             

    print sum
 
main()