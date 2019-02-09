import math

xa = int(input())
ya = int(input())
xb = int(input())
yb = int(input())

distancia = math.sqrt(((xb - xa) ** 2) + ((yb - ya) ** 2))

if distancia >= 10:
    print("longe")
else: 
    print("perto")