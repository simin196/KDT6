X = int(input()) # 총 금액
n = int(input())
total= 0
for i in range(1, n+1):
    A,B = map(int,(input().split(' ')))
    total = total + (A*B)

if X == total:
    print('Yes')
else:
    print('No')