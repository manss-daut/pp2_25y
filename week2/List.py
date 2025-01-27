#list is a container
thislist = ["apple", "banana", "cherry"]
print(thislist)
#list can be changed
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
#to determine how many items in list
print(len(thislist))
#list can contain as int, as string, as boolean values
list1 = ["abc", 34, True, 40, "male"]
#as in c++ give the type of container
thislist = list(("apple", "banana", "cherry")) #note the double round-brackets
print(thislist)
#as in string we can indexing the list
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#negatives start from -1 and that last num
print(thislist[-1])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[:4])
#we can change the list as we want
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
#and also inserting it in position
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
#also for adding we can use
#append to add in the end
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#and extend to combine containers, not only the same
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#to remove smth from list we use exactly remove
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#if we have two or more same values it removes only first
#use pop to delete specified index not value
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#but if not specified, it will delete last one
#and clear that makes list empty
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
#use of loops for list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#to loop by index
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
#and loop while
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
#in python we have sort and reverse functions
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
#reversing sorted list, and we can create own func for sort
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
#and reversing
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
#for copying list we can use copy
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#to join list or combine we can use extend as befor or plusnig them
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
