from abc import ABC,abstractmethod
# from abstract import CSVSort
import pandas as pd
import csv

df = pd.read_csv('real-estate.csv')

print(df.to_string())
print(df.dtypes)

rows = []
data=[]

with open('real-estate.csv', 'r') as csvfile:
	csvreader = csv.reader(csvfile)
	fields = next(csvreader)
	for row in csvreader:
		rows.append(row)
	print("Total no. of rows: %d"%(csvreader.line_num))
class CSVSort(ABC):
    @abstractmethod
    def sortData(self):
        pass
class SortData(CSVSort):
    def  __init__(self, data):
        self.data = data
    def sortData(self):
        if len(self.data) >1:
            m = len(self.data)//2
            l =  self.data[1:m]
            r = self.data[m:]
            lSort = SortData(l)
            lSort.sortData()
            rSort = SortData(r)
            rSort.sortData()
            i = j=k=0
            while i < len(l) and j < len(r):
                if l[i][1] < r[j][1]:
                    self.data[k] = l[i]
                    i +=1
                
                else:
                    self.data[k]=r[j]
                    j+=1
                k+=1
            
            while i < len(l):
                self.data[k] = l[i]
                i+=1
                k+=1
            
            while j < len(r):
                self.data[k] = r[j]
                j+=1
                k+=1
        
        print(self.data)
with open('real-estate.csv', 'r') as file:
            reader = csv.reader(file)
            data.extend(list(reader))
sorted = SortData(data)
print(sorted.sortData())

filename = "real-estate.csv"
# writing to csv file
with open(filename, 'w') as csvfile:
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow(fields)
	
	csvwriter.writerows(rows)

class SearchCSV(CSVSort):
    def __init__(self,lys, val, get):
        self.lys =lys
        self.val =val
        self.get = get

    def BinarySearch(self):
        first = 0
        last = len(self.lys)-1

        while first <= last:
            mid = (first +last) //2
            if self.val == self.lys[mid][self.get]:
                return mid
            else:
                if self.val < self.lys[mid][self.get]:
                   last = mid -1 
                if self.val > self.lys[mid][self.get]:              
                    first = mid +1

    def __str__(self) -> str:    
        print(self.val)



