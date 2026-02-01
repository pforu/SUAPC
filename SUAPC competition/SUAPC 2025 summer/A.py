import sys
input= sys.stdin.readline

n, m, a, b = map(int, input().split())
chair= n*3 - m #필요의자
if chair<=0:
    money= 0
else:
    money= chair*a + b

print(money)