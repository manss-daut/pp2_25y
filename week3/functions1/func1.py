def converter():
    grams = int(input("Grams: "))
    ounces = grams / 28.3495231
    return ounces
result = converter()
print(result)