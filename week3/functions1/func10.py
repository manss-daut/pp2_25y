def unique():
    clonelist = []
    for i in s:
        if i not in clonelist:
            clonelist.append(i)
    return clonelist
myinput = (input())
mylist = myinput.split()
s = [int(x) for x in mylist]
print(unique())