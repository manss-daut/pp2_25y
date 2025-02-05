word = input()
def palindrome():
    revword = "".join(reversed(word))
    if revword == word:
        print('Is a palindrome')
    else: print('Not a palindrome')
palindrome()