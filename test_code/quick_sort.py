def quick_sort(a):
    if len(a) <= 0:
        return
    barrier = a[0]
    left, mid, right = [] , [], []
    for x in a:
        if x < barrier:
            left.append(x)
        elif x == barrier:
            mid.append(x)
        else:
            right.append(x)
    quick_sort(left)
    quick_sort(right)
    k = 0
    for x in left + mid + right:
        a[k] = x
        k += 1


lst = [ -2 , 1, 2, 7, 1, 11]
quick_sort(lst)
print(lst)
