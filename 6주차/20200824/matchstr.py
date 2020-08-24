def findpossition(h,n):
    a=len(h);b=len(n);ret=[]
    for i in range(a-b+1):
        for j in range(b):
            if n[j]!=h[i+j]:break
        else:ret.append(i)
    return ret

print(findpossition('aaavvvvvdddd','ddd'))