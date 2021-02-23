
def modeNumber(myArray):
    maxi = 0;
    m_num = 0;
    for x in range(len(myArray)):
        num = myArray.count(myArray[x])
        if maxi < num:
            maxi = num;
            m_num = myArray[x]
    return m_num;

def meanNumber(myArray):
    total = 0;
    for x in range(len(myArray)):
        total = total + myArray[x];
    after_division = total/len(myArray);
    return after_division;

def medianNumber(myArray):
    mid_num = 0;
    divide_num = 0;
    if(len(myArray) % 2 == 0):
        divide_num = round((len(myArray) - 1) / 2);
        first_num = myArray[divide_num];
        second_num = myArray[divide_num + 1];
        mid_num = (first_num + second_num) / 2;
    else:
        mid_num = myArray[round((len(myArray) - 1) / 2)];
    return mid_num;

print(modeNumber([2, 3, 4, 2, 5, 4, 1, 4, 6, 4, 1, 1, 1, 1, 1]));