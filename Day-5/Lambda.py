slist =[1,2,3,4,5,6]
def sum_ele(a):
    m = 0
    for i in range(len(a)):
        m = m+a[i]
    return m
print(sum_ele(slist))

print(list(map(lambda X : X**X,slist)))