import math
Bhaskara=list(input().split())
a=float(Bhaskara[0])
b=float(Bhaskara[1])
c=float(Bhaskara[2])

if ((b * b) - 4 * a * c) < 0 or a == 0:
     print("Impossivel calcular");
else:
    t=math.sqrt((b * b) - 4 * a * c)
    R1=(-b + t) / (2 * a)
    R2=(-b - t) / (2 * a)
    print("R1 = {:.5f}\nR2 = {:.5f}".format(R1,R2))
    



