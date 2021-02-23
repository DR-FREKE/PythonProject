def veryBigInt(arr):
    total = 0
    for num in range(len(arr)):
        to_long = arr[num]
        total += to_long
    return total


print(veryBigInt([1000000001, 1000000002, 1000000003, 1000000004, 1000000005]))
