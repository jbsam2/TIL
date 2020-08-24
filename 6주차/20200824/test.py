d=["ZRO","ONE","TWO","THR","FOR","FIV","SIX","SVN","EGT","NIN"]
for t in range(int(input())):
    input();n=list(input().split());r=[0]*10
    for i in n:r[d.index(i)]+=1
    print(f'#{t+1}')
    for i,j in enumerate(r):
        while j:print(d[i],end=' ');j-=1