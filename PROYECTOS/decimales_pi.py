import os
from decimal import *
import math

r=Decimal(0)
k=0
getcontext().prec=1000
while True:
    #r += 4*(pow(-1, k)/Decimal(2*k+1))
    r += Decimal((Decimal(1)/(12/Decimal(math.sqrt(pow(640320,3))))*(Decimal((Decimal((pow(-1,k))*(math.factorial(6*k))*(13591409+545140134*k))/(Decimal((math.factorial(3*k))*(pow((math.factorial(k)),3))*(pow(640320,3*k)))))))))
    k += 1
    os.system("cls")
    print(r)