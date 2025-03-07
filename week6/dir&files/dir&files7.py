import os
def copipaster(origin_path, my_copy):
    if os.path.exists(origin_path):
        print("Path exists")
    else: 
        print("Path doesn't exist")
        return
    with open(origin_path, 'r', encoding='utf-8') as origin:
        content = origin.read()
    with open(my_copy, 'w', encoding='utf-8') as copy:
        copy.write(content)
    print(f'Copied {origin_path} to {my_copy}')
origin_path = input("What file u want to copy:")
my_copy = input("File in which u want to put ur copy or create a copy file:")
copipaster(origin_path, my_copy)