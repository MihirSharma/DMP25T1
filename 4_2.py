import math

x1 = math.radians(float(input("Enter point 1's latitude in degrees : ")))
y1 = math.radians(float(input("Enter point 1's longitude in degrees : ")))
x2 = math.radians(float(input("Enter point 2's latitude in degrees : ")))
y2 = math.radians(float(input("Enter point 2's longitude in degrees : ")))

d = 6371.01 * math.acos(math.sin(x1)*math.sin(x2) + math.cos(x1)*math.cos(x2)* math.cos(y2-y1))

print(f"The distance between the two points is {d} km")