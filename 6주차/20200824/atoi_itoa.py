def atoi(a):
    l=len(a);r=0
    for i in a:r+=(ord(i)-ord('0'))*(10**(l-1));l-=1
    return r

def itoa(n):
    a=''
    while n:a+=chr(n%10+ord('0'));n//=10
    return a[::-1]

print(atoi('1234'))
print(type(atoi('1234')))

print(itoa(1234))
print(type(itoa(1234)))