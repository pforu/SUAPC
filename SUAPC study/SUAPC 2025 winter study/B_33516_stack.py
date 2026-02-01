"""import sys
input= sys.stdin.readline

n= int(input())
cnt=0
string= list(input())

stack= [1]*n
top= -1

cnt_skeep=0

def not_empty():
    return top!=-1

def push(item):
    global top
    top+=1
    stack[top]= item

def pop():
    global top
    if not_empty():
        top-=1

def peak():
    if not_empty():
        return stack[top]
    else:
        return -1
    
def peak_before():
    if top>0:
        return stack[top-1]
    else:
        return -1
    
def last_5_peak():
    flag= False
    if stack[top]=="p" or stack[top]==0:
        if stack[top-1]=="e" or stack[top-1]==0:
            if stack[top-2]=="e" or stack[top-2]==0:
                if stack[top-3]=="k" or stack[top-3]==0:
                    if stack[top-4]=="s":
                        flag= True
    return flag

def find_skeep():
    global cnt_skeep
    cnt_skeep+=1
    for i in range(5): pop()

e_cnt=0

for item in string:
    if item=="s":
        push(item)

    elif item=="k":
        if peak()=="s" or peak()==0:
            push(item)

    elif item=="e":
        bool1= peak()=="k" or peak()==0
        bool2= peak_before()=="k" and (peak()=="e" or peak()==0)
        bool3= peak_before()==0 and (peak()=="e" or peak()==0)
        if bool1 or bool2 or bool3:
            push(item)
    
    elif item=="p":
        bool1= peak()=="e" or peak()==0
        bool2= peak_before()=="e" or peak_before()==0
        if bool1 and bool2:
            push(item)
            find_skeep()
            push(0)
            while top>=4:
                flag= last_5_peak()
                if flag:
                    find_skeep()
                else:
                    break

    #print(stack)

print(cnt_skeep)"""


"""
import sys
input= sys.stdin.readline

n= int(input())
cnt=0
stringlst= list(input())

stack= [1]*n
top= -1

cnt_skeep=0

def not_empty():
    return top!=-1

def push(item):
    global top
    top+=1
    stack[top]= item

def pop():
    global top
    if not_empty():
        top-=1

def peak():
    if not_empty():
        return stack[top]
    else:
        return -1
    
def peak_before():
    if top>0:
        return stack[top-1]
    else:
        return -1
    
def peak_be_before():
    if top>1:
        return stack[top-2]
    else:
        return -1

def find_skeep():
    global cnt_skeep
    cnt_skeep+=1
    for i in range(5): pop()

flag= False
while True:
    for item in stringlst:
        if item=="s":
            push(item)

        elif item=="k":
            if peak()=="s" or peak()==0:
                push(item)

        elif item=="e":
            bool1= peak()=="k" or peak()==0
            bool2= peak_before()=="k" and (peak()=="e" or peak()==0)
            bool3= peak_before()==0 and (peak()=="e" or peak()==0)

            if bool1 or bool2 or bool3:
                push(item)
        
        elif item=="p":
            bool1= peak()=="e" or peak()==0
            bool2= peak_before()=="e" or peak_before()==0
            bool3= peak_be_before()!="e"
            
            if bool1 and bool2 and bool3:
                push(item)
                find_skeep()
                flag=True
                push(0)

    stringlst=[]
    for i in range(top+1):
        stringlst.append(stack[i])

    if flag==False:
        break
    
    flag=False
    top=0

    #print(stringlst)

print(cnt_skeep)"""


import sys
input= sys.stdin.readline

n= int(input())
cnt=0
string= list(input())

stack= [1]*n
top= -1

cnt_skeep=0

def not_empty():
    return top!=-1

def push(item):
    global top
    top+=1
    stack[top]= item

def pop():
    global top
    if not_empty():
        top-=1

def peak():
    if not_empty():
        return stack[top]
    else:
        return -1
    
def peak_before():
    if top>0:
        return stack[top-1]
    else:
        return -1
    
def peak_be_before():
    if top>1:
        return stack[top-2]
    else:
        return -1
    
def last_5_peak():
    flag= False
    if stack[top]=="p" or stack[top]==0:
        if stack[top-1]=="e" or stack[top-1]==0:
            if stack[top-2]=="e" or stack[top-2]==0:
                if stack[top-3]=="k" or stack[top-3]==0:
                    if stack[top-4]=="s":
                        flag= True
    return flag

def find_skeep():
    global cnt_skeep
    cnt_skeep+=1
    for i in range(5): pop()


for item in string:
    if item=="s":
        push(item)

    elif item=="k":
        if peak()=="s" or peak()==0:
            push(item)

    elif item=="e":
        bool1= peak()=="k" or peak()==0
        bool2= peak_before()=="k" or peak_before()==0
        bool3= peak()=="e" or peak()==0
        bool4= peak_be_before()!="e"

        if bool1 or (bool2 and bool3 and bool4):
            push(item)
        
    elif item=="p":
        bool1= peak()=="e" or peak()==0
        bool2= peak_before()=="e" or peak_before()==0
        bool3= peak_be_before()!="e"
        
        if bool1 and bool2 and bool3:
            push(item)
            find_skeep()
            push(0)
            while top>=4:
                flag= last_5_peak()
                if flag:
                    find_skeep()
                else:
                    break

print(cnt_skeep)