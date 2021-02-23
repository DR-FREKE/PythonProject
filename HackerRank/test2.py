def staircase(n):
    stairs = ""
    for num in range(n + 1):
        if num != 0:
            stairs = " "*(n - num)
            stairs += "#"*num
            print(stairs)


staircase(6)
