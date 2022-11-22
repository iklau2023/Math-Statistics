import statistics
a= [40,50,30,40,80,60,40,40,60,30,30,50,60,70,100,40,40,90,30,40,40,60,40,60,50,40,70,40,40,30,50,40,70,60,40,40,40,60,40,60,40,40,40,40,50,60,70,40,40,60]
b= len(a)
print(f'There are {b} numbers')
c= statistics.mode(a)
d= round(statistics.mean(a))
print(f'The mode is {c}')
print(f'The average is {d}')