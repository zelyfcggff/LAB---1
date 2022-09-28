import csv

flag = 0
search = input('Введите автора: ')
f = open('result.txt', 'w')
n = 0
num = 1

with open ('books-utf8.csv', 'r', encoding='utf-8') as csvfile:
    table = csv.reader(csvfile, delimiter = ';')
    count = 0
    b = 0
    for row in table:


        if len(row[1])>30:
            b = b + 1

        lower_case = row[3].lower()
        index = lower_case.find(search.lower())
        count += 1

        if num<21:
            if row[1]!='Название':
                f.write(str(num) + '. ' + row[3] + '. ' + row[1] + ' - ' + row[6] + '\n')
                num += 1
        if (index != -1) and (float(row[7]) < 200):
            print(row[1])
            flag+=1

    if (flag == 0):
        print("Nothing found.")


f.close()
print(count)
print(b)
