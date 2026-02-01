import sys
input= sys.stdin.readline

n= int(input())
string= list(input().strip())

stack= [1]*n
top= -1

def push(item):
    global top
    top+=1
    stack[top]= item

def pop():
    global top
    top-=1

def pop_skeep():
    for _ in range(5):
        pop()
    push('A')

def is_skeep():
    if top<4:
        rst=0
    elif stack[top] != 'p' and stack[top] != 'A':
        rst=0
    elif stack[top - 1] != 'e' and stack[top - 1] != 'A':
        rst=0
    elif stack[top - 2] != 'e' and stack[top - 2] != 'A':
        rst=0
    elif stack[top - 3] != 'k' and stack[top - 3] != 'A':
        rst=0
    elif (stack[top - 4] != 's'):
        rst=0
    else:
        rst=1
    return rst


cnt_skeep= 0

for i in range(n):
    push(string[i])
    while(is_skeep()):
        pop_skeep()
        cnt_skeep+=1

print(cnt_skeep)