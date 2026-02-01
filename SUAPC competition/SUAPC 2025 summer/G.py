import sys
from collections import deque
input= sys.stdin.readline

def isPow2(n):
	return n&(n-1)==0

n= int(input())
x= list(map(int, input().split()))

m= [[0]*2*n]*2*n
cnt=[0]*2*n

for i in range(2*n):
    for j in range(2*n):
        if(isPow2(x[i]^x[j])):
            m[i][j] = 1 #banned
            m[j][i] = 1
            cnt[i]+=1
dic={}
idx=0
for i in x:
    dic[x]= [cnt, 0, idx]
    idx+=1

dic.sort(key=lambda x: x[0], reverse=True)

a=deque()
a.append(dic[0])
dic[0][1]=1
while True:
    b=deque()
    idx= b
    for i in dic:
        if m[]==1:
            i