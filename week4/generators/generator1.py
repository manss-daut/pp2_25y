def generator(n):
    num = 1
    while num < n:
        pnum = num**2
        yield pnum
        num += 1
bound = generator(int(input()))
for x in bound:
    print(x)