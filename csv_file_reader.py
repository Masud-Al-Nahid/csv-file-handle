import csv

blank_list =[]
with open('dictcsv.csv', 'r') as file:
    reader =csv.DictReader(file)
    for read in reader:
        blank_list.append(read)
print(blank_list)