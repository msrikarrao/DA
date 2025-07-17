from pickle import *
with open("zbooks.dat", 'rb') as f:
    booksList = load(f)
    for row in booksList:
        print(F"{row[0]} - {row[2]}")