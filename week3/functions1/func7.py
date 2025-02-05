myinput = (input())
mylist = myinput.split()
numbers = [int(x) for x in mylist]
def is33():
    for i in range(len(numbers) - 1):
        if numbers[i] == 3 and numbers[i + 1] == 3:
            return True
    return False
result = is33()
print(result)
