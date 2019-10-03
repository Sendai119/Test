import sys

input1 = str(sys.argv[1])

word = [" is one elfish word!", " is not an elfish word!"]

letter = "elf"


def check(a, b):
    if b == "":
        return str(a) + word[0]
    elif b[0] in a:
        return check(a, b[1:])
    return str(a) + word[1]


print check(input1, letter)
