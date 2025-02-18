def downGenerator(n):
    num = n
    while num > -1:
        yield num
        num -= 1
bound = downGenerator(int(input()))
for x in bound:
    print(x)