string = str(input())
counter_A = 0
counter_a = 0 
for i in string:
    if i.isupper():
        counter_A += 1
    elif i.islower():
        counter_a += 1
print(f'Upper case: {counter_A}')
print(f'Lower case: {counter_a}')