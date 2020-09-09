def push(num,i):
    if tree[i]:
        if num>tree[i]:push(num,2*i+1)
        else:push(num,2*i)
    else:tree[i]=num
l=[*map(int,input().split())]
tree=[0]*(100)
for i in l:
    push(i,1)
print(tree)