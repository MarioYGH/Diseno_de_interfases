 
def for2(i,j,k):
    i = i
    j = i+j
    k = not(i and k) 
    print (i)
    for2(i,j,k)
    return i

for2(1,1,3)
 
