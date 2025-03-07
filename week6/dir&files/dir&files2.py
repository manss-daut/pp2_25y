import os
def checker(path):
    print(path)
    if os.path.exists(path):
        print("Path exists")
    else: 
        print("Path doesn't exist")
        return
    if os.access(path, os.R_OK):
        print("Path is readable")
    else:
        print("Path isn't readable")
    if os.access(path, os.W_OK):
        print("Path can be written")
    else:
        print("Path can't be written")
    if os.access(path, os.X_OK):
            print("Path is executable")
    else:
            print("Path isn't executable")
tester = input("Your path:")
checker(tester)
