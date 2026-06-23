from functools import reduce
slist =[1,2,3,4,5,6]
def sum_ele(a):
    m = 0
    for i in range(len(a)):
        m = m+a[i]
    return m
print(sum_ele(slist))

print(list(map(lambda X : X*X,slist))) #multply

print(list(filter(lambda Val: Val%2!=0,slist))) # odd

print(reduce(lambda X, Y: X+Y,slist)) #sum

print(reduce(lambda X, Y: X*Y,slist)) #porduct

xlist = [["xyz",1],["pqr",3],["klm",2],["abc",4]]
print(sorted( xlist, key = lambda X:X[1])) #sorting in order
