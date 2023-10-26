import math
def polygon(sides, length):
    area = (sides * length**2) / (4 * math.tan(math.pi / sides))
    return area
sides = int(input())
length = int(input())
area = polygon(sides, length)
print(area)
