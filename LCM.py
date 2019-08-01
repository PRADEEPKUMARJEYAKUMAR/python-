pq,b=map(int,input().split())
if(pq>b):
    big=pq
else:
    big=b
while(True):
    if(big%pq==0 and big%b==0):
        lcm=big
        break
    big+=1
print(lcm)
