def camelcase(s):
    isCapital = []
    new_array = []
    for m in range(len(s)):
        if(s[m].isupper()):
            isCapital.append(s[m])

    print(len(isCapital) + 1)


camelcase('saveChangesInTheEditor')
