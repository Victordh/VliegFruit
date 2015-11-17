x = 23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15 ,16, 17, 21, 3, 4, 9
x = list(x)
y = 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
y = list(y)

def wp1_bubble(blist):
    cmpcount, swapcount = 0, 0
    while True:
        swapped = False
        for i in range(1, len(blist)):
            print cmpcount
            cmpcount += 1
            if blist[i-1] > blist[i]:
                swapcount += 1
                blist[i-1], blist[i] = blist[i], blist[i-1]
                swapped = True
        if not swapped:
            break
    return blist, cmpcount, swapcount

print wp1_bubble(x)    