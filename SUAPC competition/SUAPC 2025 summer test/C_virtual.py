import sys
from collections import deque
input= sys.stdin.readline

n= int(input())
lst= list(map(int, input().split()))
q= int(input())
query = sys.stdin.buffer.read().decode().replace('\r', '').split('\n')

rstlist= []
queue= deque(lst)

# a, b, c, x, d, e 
# d, e, x, a, b, c

# a, b, c, d, e
# b
# c, d, e, b, a
# d
# e, b, a, d, c

#             a, b, c, d, e
#                b                 (2)
#       c, d, e, b, a
#          d                       (2, 4)
# e, b, a, d, c

# 1, 2, 3, 4, 5
# 3, 4, 5, 2, 1 (2)
# 2, 1, 5, 3, 4 (5)
# 1, 5, 3, 4, 2 (2)
# 2, 4, 1, 5, 3 (4)

0 i z
(0~i-1) +(z-i+1)
(i) z-i
(i~z) -(i+1)



  #  SF(PF)는 x=1일 때의 SM(PM)
  #  SL(PL)는 x=n일 때의 SM(PM)

# 1, 2, 3, 4, 5 (3)
# 5, 4, 3, 2, 1 (3을 축으로 뒤집기)
# 4, 5, 3, 1, 2 (축 기준 앞뒤 길이 측정, 길이//2의 인덱스 기준으로 각각 뒤집기)

def flip(axis):

def pop(axis):


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