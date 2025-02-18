import math
n = int(input("Input number of sides: "))
l = int(input("Input the length of a side: "))
area = (n * l**2) / (4 * math.tan(math.pi / n))
print(f"The area of the polygon is: {area:.0f}")