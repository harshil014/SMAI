#!/usr/bin/python
import csv
def loadCsv(filename):
    lines = csv.reader(open(filename, "rb"))
    dataset = list(lines)
#    print dataset[1]
    csvfile = open('1.csv','w') 
    write = csv.writer(csvfile, delimiter=' ')
    for i in range(len(dataset)):
        for j in range(len(dataset[i])):
            if dataset[i][j] == 'NULL':
                dataset[i][j] = -1
        write.writerow(dataset[i])
    with open(filename) as f:
            z = csv.reader(f, delimiter='\t')
    return dataset

filename = 'train19.csv'
dataset = loadCsv(filename)
print('Loaded data file {0} with {1} rows').format(filename, len(dataset))
#print dataset[1]

