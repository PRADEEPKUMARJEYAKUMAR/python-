p=input()
a=("a","e","i","o","u")
count=0
for i in p:
    if(i in a):
        count=1
if(count==1):
    print("yes")
else:
    print("no")
