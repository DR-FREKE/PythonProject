# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def maxSumArray(arr: list[int])->int:
    currentSum = 0;
    maxSum = arr[0];
    sum_arr = [];
    
    for n in arr:
        if currentSum < 0:
            currentSum = 0
        currentSum += n
        
        maxSum = max(maxSum, currentSum);
    return sum_arr;

# print(maxSumArray([-2,1,-3,4,-1,2,1,-5,4]))

def subStrArr(strArr):
    count = 0
    initial_str = strArr.pop(0);
    str_split = strArr[0].split(",")
    for n in range(len(str_split)):
        if str_split[n] in initial_str:
             count = count + 1
    return -1 if count == 0 else count;

# print(subStrArr(["baseball", "exit,quit"]))

def twoStrings(s1, s2):
    # Write your code here
    str_arr1 = s1.split();
    str_arr2 = s2.split();
    A, B = str_arr1, str_arr2
    
    if len(str_arr2) > len(str_arr2):
         A, B = str_arr2, str_arr1
    
         for num in range(len(B)):
            if B[num] not in A:
                print("NO!!!")
            else:
                print("YES!!!")
twoStrings("hello world", "world hello")
