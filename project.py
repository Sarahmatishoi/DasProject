import pandas as pd
import csv
import numpy as np

df = pd.read_csv('real-estate.csv')

print(df.to_string())
print(df.dtypes)

rank = 0
file = open('real-estate.csv','r')

csv_reader = csv.reader(file,delimiter=',')

csv_list = list(csv_reader)

file1 = open('sorted_Real_Estate.csv','w+')

rows = csv_list[0]
file1.write("Rank,")
for i in rows:
    if i == rows[-1]:
        file1.write(i)
    else:
        file1.write(i + ',')
file1.write('\n')

csv_list = csv_list[1:]
csv_list.sort(key= lambda x: x[-2], reverse=True)

for i in csv_list:
    if rank == 0:
        prev_i = csv_list[csv_list.index(i)]    
        rank += 1
    else:
        prev_i = csv_list[csv_list.index(i) - 1] 
    if prev_i[-2] == i[-2]:           
        rank = rank
    else:
        rank += 1                     
    file1.write(f'{rank},')           
    for j in i:                       
        if j == i[-1] :
            file1.write(j)
        else:
            file1.write(j + ',')
    file1.write('\n')

file.close()
file1.close()