counter = 0
myList = [];
while(counter < 10):
    grade = int(input("enter a number\n"));
    if(grade % 2 != 0):
        myList.append(grade);
    counter = counter + 1;
print("\nmax odd num is:", max(myList));

def maximum(mList):
    maxi = 0;
    for x in range(len(mList)):
        if maxi < mList[x]:
            maxi = mList[x];
    return maxi;
print("miximum odd number is:", maximum(myList));