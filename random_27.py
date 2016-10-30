#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import math
probs=[0.0119742,0.0146442,0.00968193,0.00500805,0.0110194,0.0142842,0.0104199,0.00743144,0.0075259,0.0128167,0.0110148,0.00709433,0.00322201,0.0105279,0.00496812,0.0080605,0.0140531,0.00991836,0.0171892,0.009058,0.00620484,0.0155998,0.00704129,0.0079346,0.00529991,0.0130572,0.0116885,0.00191855,0.0155166,0.00683984,0.00917309,0.00814447,0.00930515,0.0121775,0.0101421,0.00303502,0.00705372,0.0138237,0.00507667,0.0114552,0.0121507,0.0230054,0.0174587,0.00602987,0.00678145,0.00776382,0.00836181,0.0133767,0.0237012,0.00725958,0.0151146,0.0111958,0.0109258,0.00279949,0.00833849,0.0127693,0.0112282,0.00434374,0.00894449,0.0139709,0.0041948,0.00663664,0.0090336,0.0055236,0.0130516,0.022237,0.00912775,0.00468499,0.0144329,0.00948629,0.0160782,0.00684038,0.0143989,0.0105485,0.00140882,0.00380973,0.00828108,0.0121637,0.00707474,0.0092504,0.006045,0.00535998,0.00863611,0.0153425,0.00865502,0.00606112,0.00494704,0.0082216,0.00348816,0.00642169,0.0110607,0.0343733,0.00665591,0.00597859,0.00954563,0.0158297,0.0116592,0.0109775,0.0165556,0.0100017]
  
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


def separateByCluster(dataset,separated):
    for i in range(1,len(dataset)):
        vector = dataset[i]
        if int(vector[-1]) not in separated:
            separated[int(vector[-1])] = []
        if(len(separated[int(vector[-1])])<probs[int(vector[-1])]):
            separated[int(vector[-1])].append(vector)
    return separated
def func(dataset):

    with open('content.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(dataset)):
            for j in range(len(dataset[i])):
                spamwriter.writerow(dataset[i][j])
      
def main():
    for i in range(len(probs)):
        probs[i]=probs[i]*1000000*3
    separated={}
    filename=['split_ac.csv','split_ad.csv','split_ae.csv','split_af.csv','split_ag.csv']
    for i in range(len(filename)):
        dataset=loadCsv(filename[i])
        separated=separateByCluster(dataset,separated)
    for i in range(len(separated)):
        print len(separated[i]),    
    func(separated)
main()