def check(s):
    return s == s[::-1]
string = str(input())
if check(string): print("Yes, it's a Palindrome")
else: print("No, it's not a Palindrome")