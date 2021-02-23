def MinMax(arr):
    arr = Sorting(arr)
    minimumCal = 0
    maximumCal = 0
    for num in range(1, len(arr)):
        maximumCal += arr[num]

    for num in range(len(arr) - 1):
        minimumCal += arr[num]
    print(minimumCal, maximumCal, end=" ")


def Sorting(arr):
    for num in range(len(arr)):
        for n in range(num+1, len(arr)):
            if arr[num] > arr[n]:
                temp = arr[n]
                arr[n] = arr[num]
                arr[num] = temp

    return arr


MinMax([2, 5, 1, 6, 1])
