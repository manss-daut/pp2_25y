myinput = (input())
mylist = myinput.split()
numbers = [int(x) for x in mylist]
def is007():
    for i in range(len(numbers) - 2):
        if numbers[i] == 0 and numbers[i + 1] == 0 and numbers[i + 2] == 7:
            return True
    return False
result = is007()
print(result)