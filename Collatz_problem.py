x= int(input('Please enter a positive intiger:'))
b= [x]
while (x !=1):  
    if ((x) % 2 == 0):
        x=(x)/2
        b.append(x)
    else:
        x=(3*x+1)
        b.append(x)
print(b)