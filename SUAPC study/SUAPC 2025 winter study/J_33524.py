'''
import sys
input = sys.stdin.readline

question, person = map(int, input().split())
level= list(map(int, input().split())).sort()
skill= list(map(int, input().split()))

q=[]
q_idx=[0]*person

for i in range(person):
    for j in range(question):
        if skill[i] < level[j]:
            q.append((j-1, i)) #최대어려운문제, 인간 
            q_idx[i]

q.sort(key=lambda x:x[0])

rst=[0]*person
idx=0
for i in range(300000):
    if 3*i*(i-1)+1 > q[idx]:
        rst[q[]]= 
'''

import sys
input = sys.stdin.readline

question, person = map(int, input().split())
level= sorted(list(map(int, input().split())))
skill= list(map(int, input().split()))

q=[]

for i in range(person):
    flag=0
    for j in range(question):
        if skill[i] < level[j]:
            q.append((j, i)) #최대어려운문제, 인간 
            flag=1
            break
    if flag==0:
        q.append((question, i))


q.sort(key=lambda x:x[0])

rst=[0]*person
idx=0

print(level)
for x in range(person):
    print(q[x])

i=0
while i<300000:
    print(f"i:{i}")
    if idx >= person:
        break

    p= q[idx]
    if p[0]==0:
        #print(f"idx:{idx}")
        rst[p[1]]= 0
        idx+=1
        i+=1
        continue

    if 3*i*(i-1)+1 > p[0]:
        #print(f"idx:{idx}")
        print(3*i*(i-1)+1, p[0])
        rst[p[1]]= i-1
        idx+=1
        i-=2
        print(f"i**:{i}")

    i+=1
    

print(' '.join(map(str, rst)))