import csv

text2 ="This Is head line"
text1 ="To protect birds from rats, it's important to take steps to prevent rats from entering your yard in the first place."

with open('demo.csv', 'w', newline="") as file:
    writer =csv.writer(file)
    writer.writerow([text2])
    for i in range(1,500):
        writer.writerow([text1])
        print(writer)
    