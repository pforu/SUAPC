import sys
from collections import deque
input= sys.stdin.readline

n= int(input())
lst= list(map(int, input().split()))
q= int(input())
query = sys.stdin.buffer.read().decode().replace('\r', '').split('\n')

rstlist= []

def SM(x):
    lst=[]
    while True:
        item= queue.popleft()
        if item==x:
            queue.append(item)
            break
        lst.append(item)
    for i in range(len(lst)):
        queue.append(lst[i])

queue= deque(lst)

for ques in query:
    if ques:
        ques= ques.split(' ')
        if ques[0]=="SF":
            queue.rotate(-1)
        elif ques[0]=="SL":
            queue.rotate(1)
        elif ques[0]=="SM":
            SM(int(ques[1]))
        elif ques[0]=="PF":
            rstlist.append(queue.popleft())
        elif ques[0]=="PL":
            rstlist.append(queue.pop())
        elif ques[0]=="PM":
            x= int(ques[1])
            queue.remove(x)
            rstlist.append(x)


print(' '.join(map(str, rstlist)))