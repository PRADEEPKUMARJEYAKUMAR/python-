p=input()
b=""
b1=""
for i in range(0,len(p)):
    if(i%2==0):
        b+=p[i]
    else:
        b1+=p[i]
print(b,b1)
