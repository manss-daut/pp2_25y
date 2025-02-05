def permutations(string, first=0):
    if first == len(string) - 1:
        print("".join(string))
        return
    for i in range(first, len(string)):
        string[first], string[i] = string[i], string[first]
        permutations(string, first + 1)
        string[i], string[first] = string[first], string[i]
string = str(input())
permutations(list(string))