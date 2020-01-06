import os
import csv

path = "" #Path would be placed here

print("Please enter the pattern:\n")
pattern = input()

if not pattern:
    print("Pattern must be provided..")

file_list = []

for r,d,files in os.walk(path):
    for file in files:
        if ".git" not in d and pattern in file:
            file_data = [file, os.path.join(r, file)]
            file_list.append(file_data)

with open('./.output/file_list.csv', mode='w') as file_list_csv:
    file_list_writer = csv.writer(file_list_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    file_list_writer.writerow(['FileName', 'FilePath'])
    for file_data in file_list:
        file_list_writer.writerow(file_data)
