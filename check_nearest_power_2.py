p=int(input())
a=0
while(a<p):
    if(p<2**a):
        b=2**a
        print(b)
        break
    a+=1
