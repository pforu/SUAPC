import sys
input= sys.stdin.readline

n= int(input())
string= list(input().strip())

stack= [1]*n
top= -1
cnt_skeep= 0
pos_s= -1
where= [0]*string.count("s")

def not_empty():
    return top!=-1

def push(item):
    global top
    top+=1
    stack[top]= item
    where[pos_s]+=1

def popall():
    global top
    top-=(where[pos_s])
    where[pos_s]=0
    


for item in string:
    flag=0

    if item=="s":
        pos_s+=1
        push(item)

    elif item=="k":
        if where[pos_s]==1:
            push(item)
        else:
            popall()

    elif item=="e":
        if where[pos_s]==2 or where[pos_s]==3:
            push(item)
        else:
            popall()

    elif item=="p":
        if where[pos_s]==4:
            push(item)
        else:
            popall()
    while True:

        if where[pos_s]==5:
            cnt_skeep+=1
            popall()
            pos_s-=1
            push(0)
        else:
            break


print(cnt_skeep)