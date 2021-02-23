def triplet(ar1, ar2):
    alicescore = 0
    bobscore = 0
    point = [0, 0]
    for num in range(len(ar1)):
        if ar1[num] > ar2[num]:
            alicescore += 1
        elif ar1[num] < ar2[num]:
            bobscore += 1
        elif ar1[num] == ar2[num]:
            alicescore = alicescore
            bobscore = bobscore
        else:
            alicescore = alicescore
            bobscore = bobscore
        point[0] = alicescore
        point[1] = bobscore
    return point


print(triplet([1, 2, 3], [3, 2, 1]))
