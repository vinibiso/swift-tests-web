def solvePagination(pg, maxRange):
    start = pg - 8
    if start < 1:
        start = 1
    stop = start + 16
    if stop > maxRange:
        stop = maxRange
    data = [ ]
    for n in range(start,stop+1):
        data.append(n)
    return data
