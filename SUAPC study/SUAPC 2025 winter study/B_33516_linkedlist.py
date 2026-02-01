import sys
input= sys.stdin.readline

n= int(input())
skeeplst= list(input())

cnt_skeep= 0
cnt_s= 0
idx_s= []

for idx in range(n):
    if skeeplst[idx]=="s":
        idx_s.append(idx)
        cnt_s+=1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(data)

    def get_node(self, index):
        cnt = 0
        node = self.head
        while cnt<index:
            cnt+=1
            node=node.next
        return node
    
    def add_node(self, index, value):
        new_node = Node(value)
        if index ==0:
            new_node.next = self.head
            self.head = new_node
            return
        node = self.get_node(index-1) 
        next_node = node.next 
        node.next = new_node 
        new_node.next = next_node 
    
    def del_node(self, index):
        if index==0:
            self.head = self.head.next
            return
        node = self.get_node(index-1)
        node.next = node.next.next

skeeplink= LinkedList(skeeplst[0])
for i in range(1, n):
    skeeplink.append(skeeplst[i])

for i in idx_s:
    k= skeeplink.get_node(i).next
    e1= k.next
    e2= e1.next
    p= e2.next
    print(p.data)

    #if k=="k" or k=="A":
    #    if e1



for i in range(0, n):
    print(skeeplink.get_node(i).data)

#while True:
#    for i in idx_s:

                        





print(cnt_skeep)