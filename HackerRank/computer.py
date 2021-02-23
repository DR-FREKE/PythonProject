def comp(x, space):
    avegra = len(space) / float(x)
    out = []
    last = 0.0

    while last < len(space):
        out.append(space[int(last): int(last + avegra)])
        last += avegra
    return out


print(comp(3, [2, 5, 4, 6, 8]))
