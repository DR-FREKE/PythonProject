import string


def Ascii(arr, word):
    alphabet_string = string.ascii_lowercase

    alphabet_list = list(alphabet_string)
    new_arr = []

    if len(arr) > 0:
        for m in range(len(word)):
            if(word[m] in alphabet_list):
                array_index = alphabet_list.index(word[m])
                new_arr.append(arr[array_index])
        sorted_array = Sorting(new_arr)
        final_result = sorted_array[len(sorted_array) - 1] * len(sorted_array)
        print(final_result)
    else:
        print('array too low')


def Sorting(arr):
    for num in range(len(arr)):
        for n in range(num+1, len(arr)):
            if arr[num] > arr[n]:
                temp = arr[n]
                arr[n] = arr[num]
                arr[num] = temp

    return arr


Ascii([1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5,
       5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7], 'zaba')
