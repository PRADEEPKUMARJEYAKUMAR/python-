p=int(input())
a=0
while(a<p):
    if(p<2**a):
        b=2**a
        print(b)
        break
    elif(p<2):
        print("2")
        break
    else:
        a+=1
