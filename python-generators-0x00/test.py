from csv import reader
with open('user_data.csv', newline='', encoding='utf-8') as file:
    content = reader(file)
    content.__next__()
    for row in content:
        print(row)