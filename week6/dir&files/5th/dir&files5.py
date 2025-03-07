my_list = ["Python", "C/C++", "Java"]
with open("answer_for_5th.txt", "w") as f:
    f.write("\n".join(my_list))
print("Check answer_for_5th.txt")
