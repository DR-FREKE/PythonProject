def PlusMinus(arr):
    positive = 0
    negative = 0
    nuetral = 0
    for num in range(len(arr)):
        if arr[num] > 0:
            positive += 1
        elif arr[num] < 0:
            negative += 1
        else:
            nuetral += 1
    positive = positive / len(arr)
    negative = negative / len(arr)
    nuetral = nuetral / len(arr)

    print(format(positive, '.6f'), format(
        negative, '.6f'), format(nuetral, '.6f'), sep="\n")


PlusMinus([-4, 3, - 9, 0, 4, 1])
