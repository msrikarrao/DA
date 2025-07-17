from csv import *
with open('zscores.csv', 'r', newline='') as f:
    fReader = reader(f)
    for row in fReader:
        print(F"{row[0]} - {row[3]}")