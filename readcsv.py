import csv;

with open('names.csv') as csv_file:
    csv_read = csv.reader(csv_file);

    header = next(csv_read);
    print(header[1]); 

    for line in csv_read:
        print(line[1]);