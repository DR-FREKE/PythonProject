def findMax(num):
    currMax = 0;
    newMax = 0;
    
    for val in range(len(num)):
        if(num[val] == 1):
            currMax += 1;
            if currMax > newMax:
                newMax = currMax
        else:
            currMax = 0;
    return newMax;
    
maxVal = findMax([1, 1, 0, 1, 1, 1])
print(maxVal)
