def histogram(s):
    for number in s:
        print('*' * number)
myinput = input()
mylist = myinput.split()
nums = []
for i in mylist:
    nums.append(int(i))
histogram(nums)