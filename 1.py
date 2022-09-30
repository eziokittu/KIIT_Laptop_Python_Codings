v=list(map(int,input().split(".")))
i=input()
if i=="MAJOR":
 v[0]=v[0]+1
elif i=="MINOR":
 v[1]+=1
elif i=="PATCH":
 v[2]+=1
print(".".join(list(map(str,v))))