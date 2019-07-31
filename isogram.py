p=input()
l=[]
count=0
l1=[]
p=list(p)
for i in p:
    if i not in l1:
        l1.append(i)
for i in l1:
    l.append(p.count(i))
for i in l:
    if(int(i)>1):
        count=1
if(count==0):
    print("Yes")
else:
    print("No")
    
