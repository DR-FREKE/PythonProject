def findmyNumber(mArrayList, number):
    if number not in mArrayList:
        return "NO";
    else:
        return "YES";

input_number = input("Enter number:\n")
print(findmyNumber([2, 5, 7, 3],int(input_number)));