import sys

input1 = int(sys.argv[1])

def digit(x):
    if (x == 0):
        return 0
    else:
        return 1 + digit(abs(x) / 10)

def digititeative(x):
    count = 0
    while (x > 0):
        x = x // 10
        count = count + 1
    return count


print "The number of digit(s) calculated by recursive is " + str(digit(input1)) + " and by iterative is " + str(digititeative(input1)) + "."