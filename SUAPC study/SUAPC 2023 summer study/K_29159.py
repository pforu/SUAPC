import sys
from fractions import Fraction
input= sys.stdin.readline

cake1_x=0
cake1_y=0
cake2_x=0
cake2_y=0

for i in range(4):
    x, y= map(int, input().split())
    cake1_x+=x
    cake1_y+=y

cake1_x= Fraction(cake1_x)/4
cake1_y= Fraction(cake1_y)/4

for i in range(4):
    x, y= map(int, input().split())
    cake2_x+=x
    cake2_y+=y

cake2_x= Fraction(cake2_x)/4
cake2_y= Fraction(cake2_y)/4

p= Fraction(Fraction(cake1_y-cake2_y)/Fraction(cake1_x-cake2_x))
q= Fraction(cake1_y - Fraction(p*cake1_x))

print(p, q)