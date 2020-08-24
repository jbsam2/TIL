def makepartialmatch(s):
    l=len(s);pi=[0]*l;begin=1;matched=0
    while begin+matched<l:
        if s[begin+matched]==n[matched]:
            matched+=1
            pi[begin+matched-1]=matched
        else:
            if matched==0:
                begin+=1
            else:
                begin+=matched-pi[matched-1]
                matched=pi[matched-1]
    return pi

def kmp(h,n):
    hl=len(h);nl=len(n);ret=[];pi=makepartialmatch(n);begin=matched=0
    while begin+nl<=hl:
        if matched<nl and h[begin+matched]==n[matched]:
            matched+=1
            if matched==nl:ret.append(begin)
        else:
            if matched==0:begin+=1
            else:
                begin+=matched-pi[matched-1]
                matched=pi[matched-1]
    return ret