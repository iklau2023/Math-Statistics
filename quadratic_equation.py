import math
import time
a= float(input("a="))
b= float(input("b="))
c= float(input("c="))
x1= ((b*-1) + math.sqrt(b**2 - 4*a*c))/2
x2= ((b*-1) - math.sqrt(b**2 - 4*a*c))/2
print(f'x= {x1} or {x2}')
time.sleep(100)
