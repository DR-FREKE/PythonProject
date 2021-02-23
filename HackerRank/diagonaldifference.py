def diagonalDiff(arr):
    left_to_right_total = 0
    right_to_left_total = 0
    sum_total = 0
    for num in range(len(arr)):
        left_to_right_total += arr[num][num]
        right_to_left_total += arr[num][len(arr) - (num+1)]
    if(left_to_right_total > right_to_left_total):
        sum_total = left_to_right_total - right_to_left_total
    else:
        sum_total = right_to_left_total - left_to_right_total
    return sum_total


print(diagonalDiff([[1, 2, 3], [2, 5, 1], [4, 9, 1]]))
