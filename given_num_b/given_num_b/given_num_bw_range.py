p=int(input())
a,b=map(int,input().split())
for i in range(a+1,b+1):
    if(i==p):
        print("yes")
        break
else:
    print("no")
