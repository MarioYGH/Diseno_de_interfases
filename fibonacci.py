import numpy as np

n = 11
x = 0
y = 1

for i in range(1,n):
    z = y + x
    y = x
    x = z
    
    print(x)
    
