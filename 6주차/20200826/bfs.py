def sol(n):
    q=[];q.append(n);visit.append(n)
    while len(q):
        node=q.pop(0);visit.append(node);print(node,end=' ')
        for i in b[node]:
            if i not in visit:visit.append(i);q.append(i)

n,m=map(int,input().split());l=list(map(int,input().split()));b=[[]for _ in range(n+1)];visit=[]
for i in range(m):s=l[2*i];e=l[1+2*i];b[s].append(e);b[e].append(s)
sol(1)