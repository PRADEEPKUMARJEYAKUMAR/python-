p,b=map(int,input().split())
a=p*b
c=a//2
d=set([c])
count=0
while c*c!=a:
    c=(c+(a//c))//2
    if c in d:
        count=1
    d.add(c)
if(count==0):
    print("yes")
else:
    print("no")
    
