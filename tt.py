import csv

with open('/Users/dmitry/dj-homeworks/databases/work_with_database/phones.csv', 'r') as csvfile:
    phone_reader = csv.DictReader(csvfile, delimiter=';')


    for i in phone_reader:
        print(i)