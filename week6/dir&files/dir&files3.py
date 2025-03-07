import os
path = input("Path:")
if os.path.exists(path):
    print("Path exists")
    directory, filename = os.path.split(path)
    print("Directory:", directory)
    print("Filename:", filename)
else : print("Path doesn't exist")