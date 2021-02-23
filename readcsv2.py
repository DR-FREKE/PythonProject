import csv;

read_file = open('names.csv');

read_csv = csv.reader(read_file);

for line in read_csv:
    print(line);