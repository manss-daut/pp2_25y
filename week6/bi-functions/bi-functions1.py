my_list = list(map(int, input().split()))
num = 1
for i in my_list:
    num *= int(i)
print(num)