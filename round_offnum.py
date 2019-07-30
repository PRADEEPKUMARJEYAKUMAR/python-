a=float(input())
for i in range(0,10):
    a=a+0.1
    b=str(a)
    c=b.find('.')
    if(b[c+1]=="0"):
        print(b[0:c])
        break
