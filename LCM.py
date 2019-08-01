p,b=map(int,input().split())
if(p>b):
    big=p
else:
    big=b
while(True):
    if(big%p==0 and big%b==0):
        lcm=big
        break
    big+=1
print(lcm)
