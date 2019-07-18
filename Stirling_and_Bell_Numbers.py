def stirling(items,category):
    if category>items:
        return 0
    elif category==items:
        return 1
    elif category==1:
        return 1
    else:
        return category*stirling(items-1,category)+stirling(items-1,category-1)
    
def bell(items):
    a=0
    for i in range(1,items+1):
        a=a+stirling(items,i)
    return a
    
    
print stirling(1,1)

print stirling(2,1)

print stirling(2,2)

print stirling(2,3)

print stirling(3,1)

print stirling(3,2)

print stirling(3,3)

print stirling(4,1)

print stirling(4,2)

print stirling(4,3)

print stirling(4,4)

print stirling(5,1)

print stirling(5,2)

print stirling(5,3)

print stirling(5,4)

print stirling(5,5)

print stirling(20,15)

print bell(1)

print bell(2)

print bell(3)

print bell(4)

print bell(5)

print bell(15)
