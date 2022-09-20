import csv

with open('./Dataset/Property.csv') as inputfile:
    data = csv.reader(inputfile)
    print(data)