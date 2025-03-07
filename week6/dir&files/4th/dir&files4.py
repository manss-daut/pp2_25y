with open("example_for_4th.txt", "r") as f:
    counter = len(f.readlines())
print("There are:", counter, "lines")