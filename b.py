import csv
i=input("enter song name:\n")
with open('test.csv','r')as f:
    data=csv.reader(f,delimiter=",")
    for row in data:
        if i==row[0]:
            print("lyrics:",row[1])
        
