import random
from django.shortcuts import render

# Create your views here.
def lotto(request):
    lucky = [3,11,34,42,43,44]
    bonus = 13
    first=second=third=fourth=fifth=bomb=0
    for i in range(1000):
        tmp = sorted(random.sample(range(1,46),6))
        cnt=0
        for j in tmp:
            if j in lucky:cnt+=1
        if cnt==6:first+=1
        elif cnt==5 and bonus in tmp:second+=1
        elif cnt==5:third+=1
        elif cnt==4:fourth+=1
        elif cnt==3:fifth+=1
        else:bomb+=1
    context = {
        'first':first,
        'second':second,
        'third':third,
        'fourth':fourth,
        'fifth':fifth,
        'bomb':bomb,
        'bonus':bonus,
        'lucky':lucky
    }

    return render(request,'lotto.html',context)