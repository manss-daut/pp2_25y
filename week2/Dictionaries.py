#dictionaries is like map in c++
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
#Dictionary items are ordered, changeable, and do not allow duplicates.
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
#you can acces exact value by key of dict
x = thisdict["age"]
print(x)
#also you can acces and print keys, values and both at once
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
y = car.values()
z = car.items()
print(x, y, z)
#we can change values by key
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)
#and change items using update
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)
#we can add items 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "white"
print(thisdict)
#or update it and so adding
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)
#as before to remove use pop, del, clear
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("year")
print(thisdict)
#popitem for last key
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
#del without exact key will delete dict completely
#and clear to nulling the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
#we can loop through both of
for x, y in thisdict.items():
  print(x, y)
#we can copy that dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
#you can create multi dictionary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
#can access for smth
print(myfamily["child2"]["name"])
#and also can loop
for x, obj in myfamily.items():
  print(x)
  for y in obj:
    print(y + ':', obj[y])
    