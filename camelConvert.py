
import numpy as np

x = input("Enter a name: ")
y = x.split()

z = []


for i in range(len(y)):
    
    if(i == 0):
        z.append(y[i].lower())
    elif (i>0): 
        z.append(y[i].capitalize())

a = ''.join(z)

print(a)
