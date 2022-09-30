v=list(map(int,input().split('.')))
i=['MAJOR','MINOR','PATCH'].index(input())
for j,x in enumerate(v):
 if i==j:v[j]+=1
 elif j>i:v[j]=0
print('.'.join(map(str,v)))