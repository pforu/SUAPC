"""import sys
input= sys.stdin.readline

MOD= 998244353
w, h, k, t= map(int, input().split())

virus= 1
for i in range(k):
    x, y= map(int, input().split())
    able_w= min(x+t, w) - max(x-t, 1) + 1
    able_h= min(y+t, h) - max(y-t, 1) + 1
    virus= (virus * (able_w*able_h % MOD)) %MOD

print(virus)"""

import sys
MOD = 998244353

#data = sys.stdin.buffer.read().replace(b'\x1a', b'')
#w, h, k, t, *rest = map(int, data.split())
w, h, k, t, *rest = map(int, sys.stdin.buffer.read().split())

virus = 1
for i in range(0, k*2, 2):
    x = rest[i]
    y = rest[i+1]
    able_w = min(x+t, w) - max(x-t, 1) + 1
    able_h = min(y+t, h) - max(y-t, 1) + 1
    able_w %= MOD
    able_h %= MOD
    able_sq = able_w * able_h % MOD
    virus = virus * able_sq % MOD

print(virus)
