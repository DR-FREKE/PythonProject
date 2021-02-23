import csv;

with open('names.csv') as read_file:
    read_csv = csv.DictReader(read_file);

    for line in read_csv:
        print(line['Email'])