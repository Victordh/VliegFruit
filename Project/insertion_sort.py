x = 23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15 ,16, 17, 21, 3, 4, 9
x = list(x)
y = 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
y = list(y)

# open overwrites the already existing file
f = open('out.txt', 'w')

def sort_numbers(s):
    count = 0
    for i in range(1, len(s)):
        val = s[i]
        j = i - 1
        while (j >= 0) and (s[j] > val):
            f.write(str(s) + "\n")
            count += 1
            temp = s[j+1]
            s[j+1] = s[j]
            s[j] = temp
            j = j - 1
    # prints final (correct) list
    f.write(str(s) + "\n")
    f.write("Amount of steps needed: " + str(count))
    return s


sort_numbers(x)
f.write("\n\n")
sort_numbers(y)

f.close()

# def main():
#     x = eval(input("Enter numbers to be sorted: "))
#     x = list(x)
#     sort_numbers(x)
#     print(x)