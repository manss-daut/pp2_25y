def squareGenerator(a, b):
    bound1 = a
    bound2 = b
    while bound1 < bound2:
        sqnum = bound1**2
        yield sqnum
        bound1 += 1
a = int(input())
b = int(input())
boundarys = squareGenerator(a, b)
for x in boundarys:
    print(x)