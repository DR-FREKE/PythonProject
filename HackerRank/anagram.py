def Anagram(dictionary, query):
    for num in range(len(query)):

        if query[num] not in dictionary:
            pass
        else:
            print(query[num])


Anagram(['hack', 'a', 'rank', 'khac', 'ackh'],
        ['a', 'nark', 'bs', 'hack', 'stairs'])
