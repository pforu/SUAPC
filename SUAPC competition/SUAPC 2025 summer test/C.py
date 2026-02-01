import sys
input= sys.stdin.readline

INIT= 300000

n= int(input())
lst= list(map(int, input().split()))
q= int(input())
query = sys.stdin.buffer.read().decode().replace('\r', '').split('\n')

#.replace(b'\x1a', b'')

rstlist= []

class Queue:
    def __init__(self, initfr, datalen):
        self.front= initfr+1
        self.rear= initfr
        self.data= [0]*datalen
    
    def enqueueR(self, item):
        self.rear+=1
        self.data[self.rear]= item

    def enqueueL(self, item):
        self.front-=1
        self.data[self.front]= item
    
    def dequeueR(self):
        rst= self.data[self.rear]
        self.rear-=1
        return rst
    
    def dequeueL(self):
        rst= self.data[self.front]
        self.front+=1
        return rst
    
    def SF(self):
        self.enqueueR(self.dequeueL())

    def SL(self):
        self.enqueueL(self.dequeueR())

    def SM(self, x):
        lst=[]
        while True:
            item= self.dequeueL()
            if item==x:
                self.enqueueR(item)
                break
            lst.append(item)
        for i in range(len(lst)):
            self.enqueueR(lst[i])

    def PF(self):
        rstlist.append(self.dequeueL())

    def PL(self):
        rstlist.append(self.dequeueR())

    def PM(self, x):
        lst=[]
        while True:
            item= self.dequeueR()
            if item==x:
                rstlist.append(item)
                break
            lst.append(item)
        for i in range(len(lst)-1, -1, -1):
            self.enqueueR(lst[i])


queue= Queue(-1, n*2)
for i in range(n):
    queue.enqueueR(lst[i])
#print(queue.rear)


#print(f"{queue.front} < {queue.data} > {queue.rear}")


for ques in query:
    ques= ques.split(' ')
    #print("ques:", ques)
    if ques[0]=="SF":
        queue.SF()
    elif ques[0]=="SL":
        queue.SL()
    elif ques[0]=="SM":
        queue.SM(int(ques[1]))
    elif ques[0]=="PF":
        queue.PF()
    elif ques[0]=="PL":
        queue.PL()
    elif ques[0]=="PM":
        queue.PM(int(ques[1]))
    #print(f"{queue.front} < {queue.data} > {queue.rear}  :  {rstlist}")


print(' '.join(map(str, rstlist)))

'''
1 5 2 4 3
2 4 3 5 1
4 3 5 1 (2)
1 4 3 5 (2)
1 4 3 (2, 5)
4 3 1 (2, 5)
4 1 (2, 5, 3)
1 4 (2, 5, 3)
1 (2, 5, 3, 4)
(2, 5, 3, 4, 1)

'''