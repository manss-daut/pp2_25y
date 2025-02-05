def temperature():
    F = int(input("Farenheits: "))
    C = (5 / 9) * (F - 32)
    return C
result = temperature()
print(result)