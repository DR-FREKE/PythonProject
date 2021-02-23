def Scores(arr):
    new_array = []
    for m in range(len(arr)):
        if(arr[m] >= 38):
            remainder = arr[m] % 5
            remainder_calc = 5 - remainder
            if(remainder_calc < 3):
                new_score = arr[m] + remainder_calc
                new_array.append(new_score)
            else:
                new_array.append(arr[m])
        else:
            new_array.append(arr[m])
    return new_array


print(Scores([4, 73, 67, 38, 33]))
