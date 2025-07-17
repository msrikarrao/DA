# A two-dimensional list with 5 rows and 3 columns.
books = [
    ["Book Name", "Author Name", "Price"],
    ["Attitude", "John C Maxwell", 10.99],
    ["The Power of Now", "Eckhart Tolle", 12.99],
    ["Atomic Habits", "James Clear", 15.50]
]
import pickle
# Open a binary file in write mode
with open("zbooks.dat", 'wb') as f:
    pickle.dump(books, f)