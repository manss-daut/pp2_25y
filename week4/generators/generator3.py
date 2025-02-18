def generator34(n):
    num = 0
    while num < n:
        if num % 3 == 0 and num % 4 == 0:
            yield num
        num += 1
bound = generator34(int(input()))
for x in bound:
    print(x)