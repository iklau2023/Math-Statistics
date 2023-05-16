import math
R= float(input('Radius: '))
L= float(input('Length: '))
X= float(input('Height: '))

Y= 1.3*(math.sqrt(1-((X**2)/L**2)))
print(Y*2)

