p,b=map(int,input().split())
l=[]
l1=[]
for i in range(1,p):
    if(p%i==0):
        l.append(i)
for i in range(1,b):
    if(b%i==0):
        l1.append(i)
q=[]
for i in l:
        q.append(i)
for i in l1:
    q.append(i)
w=1
#print(l,l1,q)
for i in q:
    w*=int(i)
print(w)
