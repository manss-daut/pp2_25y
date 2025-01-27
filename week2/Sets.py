#sets is unordered, unchangable but smth can be added or removed, and unidexed, and set is culy(?) braces{}
#set is unordered so can be aby order
thisset = {"apple", "banana", "cherry"}
print(thisset)
#in set duplicates are ignores
thisset1 = {"apple", "banana", "orange", "orange"}
print(thisset1)
#to add another set in set use update instead of extend
thissett = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thissett.update(tropical)
print(thisset)
#to add smth use simply add
thisset2 = {"apple", "banana", "cherry"}
thisset2.add("orange")
print(thisset2)
#to remove smth we use discard
thisset4 = {"apple", "banana", "cherry"}
thisset4.discard("banana")
print(thisset4)
#we can loop though the set
thisset5 = {"apple", "banana", "cherry"}
for x in thisset5:
  print(x)
#joinning sets
#unoin or |
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
set4 = set1 | set2
print(set3, set4)#they do same thing
#to union multiple sets just write after comma or |
#also union allows to combine with other container but not |
#intersection and & will give us only same in both sets
set1x = {"apple", "banana", "cherry"}
set2x = {"google", "microsoft", "apple"}

set3x = set1x.intersection(set2x)
set4x = set1x & set2x
print(set3x, set4x)
#difference or - will give us elements from frist that not in second
set1y = {"apple", "banana", "cherry"}
set2y = {"google", "microsoft", "apple"}

set3y = set1y.difference(set2y)
set4y = set1y - set2y
print(set3y, set4y)
#and symmetric_difference that give us elements are not in both
set1z = {"apple", "banana", "cherry"}
set2z = {"google", "microsoft", "apple"}

set3z = set1z.symmetric_difference(set2z)
set4z = set1z ^ set2z
print(set3z, set4z)
