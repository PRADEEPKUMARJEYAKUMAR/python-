a=input()
b=len(a)
c=b//2
b1=[]
for i in range(len(a)):
    if(b%2==1):
        if(c==i):
            i="*"
            b1.append(i)
        else:
            b1.append(a[i])
    else:
        if(c==i or (c-1)==i):
            i="*"
            b1.append(i)
        else:
            b1.append(a[i])
print(''.join(b1))   
