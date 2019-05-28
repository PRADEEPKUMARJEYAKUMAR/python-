l=list(map(int,input().split()))
a={i:l.count(i) for i in l}
for x,y in a.items():
  print(x,y)
