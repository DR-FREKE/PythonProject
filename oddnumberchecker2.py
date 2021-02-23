mylist = [];
oddList = [];

while (len(mylist) < 10):
    input_fld = int(input("enter a number \n"));
    mylist.append(input_fld);

for newList in mylist:
    if(newList % 2 != 0):
        oddList.append(newList);
print(max(oddList));