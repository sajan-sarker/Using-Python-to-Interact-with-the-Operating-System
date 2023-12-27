import csv

file = open("./Module 2/data.csv")
file_csv = csv.reader(file)

for rows in file_csv:
    id, name, email, number = rows
    print(f'ID: {id :>5}, Name: {name :>5} , Email: {email:>16}, Number: {number }')

file.close()