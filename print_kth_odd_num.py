p,b=map(int,input().split())
a=list(map(int,input().split()))
for i in a:
    if(a[b]//2==1 and b<=len(a)):
        print(a[b])
        break
    b+=1
