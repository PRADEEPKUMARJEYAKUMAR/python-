p,b=map(int,input().split())
l=[]
l1=[]
for i in range(1,p+1):
    if(p%i==0):
        l.append(i)
for i in range(1,b+1):
    if(b%i==0):
        l1.append(i)
q=[]
for i in l:
    if(i in l1):
        q.append(i)
print(q[-1])
        
