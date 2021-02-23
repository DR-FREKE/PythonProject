def numPlayers(k, scores):
    main_score = Sorting(scores)
    rank_array = []
    total_length = 0
    for num in range(len(main_score)):
        if main_score.index(main_score[num]) <= k:
            rank_array.append((k - num) + 1)
        # rank_array.append(k - main_score.index(
        #     main_score[num]) + 1)
        # if rank_array[num] <= k:
        #     total_length += 1
    return rank_array


def Sorting(arr):
    for num in range(len(arr)):
        for n in range(num+1, len(arr)):
            if arr[num] > arr[n]:
                temp = arr[n]
                arr[n] = arr[num]
                arr[num] = temp

    return arr


print(numPlayers(4, [2, 2, 3, 4, 5]))
