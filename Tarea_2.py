
# for sin usar for ni ninguna funcion

#i inicio
#j es el paso
#k es la condicion
def for2(i, j, k):
    print(i)
    i = i + j
    return (i <= k and [for2(i, j, k)]) 

for2(0, 2, 8)

#Creo que así va con otra condicion xd
# def for2(i, j, k, cond):
#     print(i)
#     i = i + j
#     return (cond(i, k) and for2(i, j, k, cond)) 

# def condition(x, y):
#     return x == y
