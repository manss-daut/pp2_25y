myinput = (input())
mylist = myinput.split()
numbers = [int(x) for x in mylist]
def filter_prime(numbers):
    itslist = []
    for x in numbers:
        if x < 2:
            continue
        itsprime = True
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                itsprime = False
                break
        if itsprime:
            itslist.append(x)
    return itslist
result = filter_prime(numbers)
print(result)
