import csv

students = {
    
    'Name':'Masud al Nahid',
    'City' : "Khulna",
    'Village': 'Khoksha',
    'Favriate Pet': 'Badgriger',
    'Email': 'mdmsd2@gmail.com',
    'Phone Number': +8801713423454    
}

with open('dictcsv.csv', 'w', newline='', encoding='utf-8') as file:
    writer =csv.DictWriter(file, fieldnames=students.keys())
    writer.writeheader()
    i=0
    while i < 5000:
        writer.writerow(students)
        i+=1
    