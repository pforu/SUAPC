import sys
input= sys.stdin.readline

INIT= 300000

n= int(input())
lst= list(map(int, input().split()))
q= int(input())
query = sys.stdin.buffer.read().decode().replace('\r', '').split('\n')

rstlist= []

class Queue:
    def __init__(self, initfr, datalen):
        self.front= initfr
        self.rear= initfr-1
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


queue= Queue(INIT*2, INIT*5)
for i in range(n):
    queue.enqueueR(lst[i])

for ques in query:
    if ques:
        ques= ques.split(' ')
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


print(' '.join(map(str, rstlist)))