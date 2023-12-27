import csv

data = [['name', 'email', 'number'], ['John', 'john@gmail.com', '1234567890'], 
        ['Jack', 'jack@gmail.com', '0987654321']]

with open('./Module 2/info.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(data)