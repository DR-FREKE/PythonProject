counter = 0;
total = 0;
while counter < 10:
    grade = int(input("enter your number\n"));
    total = total + grade;
    counter = counter + 1;
average = total/10;
print(average);