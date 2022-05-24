The idea of this algorithm is to sort two different sorted array into one. I used the pointing end technique for this.
NOTE:I'm trying to come up with my own different ways to solve problems.

def sortTwoSortedArrays(arr1, arr2):
    new_arr = [];
    arr_len = 0;
    if len(arr1) > len(arr2):
        arr_len = len(arr1) - 1;
    else:
        arr_len = len(arr2) - 1
    
    start_one = 0;
    start_two = 0;
        
    while start_one < arr_len or start_two < arr_len:
        if arr1[start_one] < arr2[start_two]:
            new_arr.append(arr1[start_one])
            start_one += 1;
        else:
            new_arr.append(arr2[start_two])
            start_two += 1;
    return new_arr;

result = sortTwoSortedArrays([17, 21, 29, 38], [4, 9, 25, 32]);
print(result)
