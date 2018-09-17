import csv

with open('sajad.csv', 'r') as names:
    reader = csv.reader(names, quotechar='|')
    for name in reader:

        print("_".join(name[0].split()))
