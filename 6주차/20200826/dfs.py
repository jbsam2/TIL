def sol1(n):
    visit1.append(n);print(n,end=' ')
    for i in b[n]:
        if i not in visit1:sol1(i)


def sol2(n):
    stack=[]
    stack.append(1)
    while len(stack):
        v=stack.pop()
        if v not in visit2:
            print(v,end=' ')
            visit2.append(v)
            for i in b[v]:
                if i not in visit2:
                    stack.append(i)

n,m=map(int,input().split());l=list(map(int,input().split()));b=[[]for _ in range(n+1)];visit1=[];visit2=[]
for i in range(m):s=l[2*i];e=l[1+2*i];b[s].append(e);b[e].append(s)
sol1(1)
print()
sol2(1)