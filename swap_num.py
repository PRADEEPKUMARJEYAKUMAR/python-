p=input()
k=0
n=1
for i in range(0,len(p)//2):
        print(p[n]+p[k],end="")
        k+=2
        n+=2
