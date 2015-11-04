y = 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
y = list(y)

# open overwrites the already existing file
f = open('out.txt', 'w')

def big_flip(s):
    # TODO make count global and don't reset it when combining different sorts
    count = 1
    length = len(s)
    # prints first (incorrect) list
    f.write(str(s) + "\n")
    for i in range(0, length / 2):
        temp = s[length - i - 1]
        s[length - i - 1] = s[i]
        s[i] = temp
    # prints final (correct) list
    f.write(str(s) + "\n")
    f.write("Amount of steps needed: " + str(count))
    return s
        
f.write("\n\n")
big_flip(y)

f.close()