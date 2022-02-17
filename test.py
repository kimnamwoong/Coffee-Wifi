import csv


with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',')
    list_of_rows = []
    for row in csv_data:
        list_of_rows.append(row)

# for i in list_of_rows:
#     print(i)

# print(list_of_rows[0])
for cafe in list_of_rows:
    for item in cafe:
        if item[:4] == "http":
            print("Maps link")


