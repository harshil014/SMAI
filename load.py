#!/usr/bin/python
import csv
def loadCsv(filename):
	lines = csv.reader(open(filename, "rb"))
	dataset = list(lines)
	print dataset[1]
	for i in range(len(dataset)):
		for j in range(len(dataset[i])):
			if dataset[i][j] == 'NULL':
				dataset[i][j] = float(-1)
			else:
				dataset[i][j] = float(dataset[i][j])
	#	dataset[i] = [float(x) for x in dataset[i] if x not in ['NULL']]
	return dataset


filename = 'set.csv'
dataset = loadCsv(filename)
print('Loaded data file {0} with {1} rows').format(filename, len(dataset))
print dataset[1]
