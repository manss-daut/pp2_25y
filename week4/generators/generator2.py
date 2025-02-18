def evenGenerator(n):
    num = 0
    while num < n:
        yield num
        num += 2
bound = evenGenerator(int(input()))
print(", ".join(str(x) for x in bound))