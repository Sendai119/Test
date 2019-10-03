import sys

input1 = int(sys.argv[1])


def sumofrecursive(x):
    if x == 0:
        return 0
    else:
        return sumofrecursive(x - 1) + x


def sumofiterative(x):
    if x == 0:
        return 1
    else:
        count = 0
        for i in range(1, x + 1):
            count = count + i
        return count


print "The SUM value calculated by recursive is " + str(sumofrecursive(input1)) + " and by iterative is " + str(
    sumofiterative(input1)) + "."
