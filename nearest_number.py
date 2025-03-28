#finding nearest number
a=[1,2,5,7,8,10,12,15,16,19,20,21,22,29,31]
b=11  

def nearest_number(a,b):
    l,r = 0, len(a) - 1
    
    while l<=r:
        mid = (l+r) // 2
        if a[mid] == b:
            return a[mid]
        elif a[mid] < b:
            l= mid + 1
        else:
            r = mid - 1
    
    if l >= len(a):
        return a[r]
    if r < 0:
        return a[l]
    
    if abs(a[l]- b)<abs(a[r]-b):
        return a[l]
    if abs(a[l]- b)==abs(a[r]-b):
        return a[r],a[l]
    else:
        return a[r]


print(nearest_number(a,b))
