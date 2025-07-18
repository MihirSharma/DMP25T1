import math

c1r = int(input("Circle 1 : Radius = "))
c1x = int(input("Circle 1 : Center X = "))
c1y = int(input("Circle 1 : Center Y = "))
c2r = int(input("Circle 2 : Radius = "))
c2x = int(input("Circle 2 : Center X = "))
c2y = int(input("Circle 2 : Center Y = "))


dist_c1c2 = math.sqrt((c1x-c2x)**2+(c1y-c2y)**2)

if(abs(c2r-c1r)>=dist_c1c2):
    print("Overlap")
elif(c2r+c1r>=dist_c1c2):
    print("Intersect")
else:
    print("No Touch")