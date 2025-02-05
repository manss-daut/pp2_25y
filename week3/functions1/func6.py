def reverser(string):
    words = string.split()
    reverse = " ".join(reversed(words))
    return reverse
string = str(input())
print(reverser(string))