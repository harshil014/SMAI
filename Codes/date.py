import csv
from datetime import datetime

#with open('content.csv','rb') as source:
#    rdr = csv.reader(source)
#    with open('result.csv','wb') as result:
#        wtr = csv.writer(result)
#        for r in rdr:
#            wtr.writerow((r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9],r[10],r[11],r[12],r[13],r[14],r[15],r[16],r[17],r[18],r[19],r[20],r[21],r[22],r[23]))

x = []
with open('result.csv','rb') as source:
    rdr = csv.reader(source)
    data = list(rdr)
    date_format = "%Y-%m-%d"
    for i in range(len(data)):
        d0 = datetime.strptime(data[i][10], date_format)
        d1 = datetime.strptime(data[i][11], date_format)
        delta = d1 - d0
        x.append(str(delta.days))

with open('result.csv','rb') as source:
    rdr = csv.reader(source)
    with open('final.csv','wb') as final:
        wtr = csv.writer(final)
        for r in rdr:
            wtr.writerow((r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9],x[i],r[12],r[13],r[14],r[15],r[16],r[17],r[18],r[19],r[20],r[21],r[22]))
        
        


