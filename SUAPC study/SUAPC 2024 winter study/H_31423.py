import sys
input= sys.stdin.readline

class Node:
    def __init__(self, data, next):
        self.data= data
        self.next= next


n= int(input())
school= [input() for _ in range(n)]
relation= [list(map(int, input().split())) for _ in range(n)]

