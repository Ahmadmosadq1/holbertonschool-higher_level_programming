import csv
with open("products.csv", "r") as file:
    reader = csv.DictReader(file)
    print(reader.fieldnames)