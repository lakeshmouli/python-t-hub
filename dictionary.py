n=int(input())#15
#5 4 3 12 54 67 2 1 54 67 34 1 2 3 2
data=list(map(int,input().split()))
data.sort()
dic={}
for i in data:
    dic[i]=1
for k,v in dic.items():
    
    print(k,end=" ")
