p=int(input())
b=list(map(int,input().split()))
s=1
for i in range(len(b)):
    if(b[i]!=s):
        print(i)
        break
    s+=1
        
