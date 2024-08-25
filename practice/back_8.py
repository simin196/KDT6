A,B,C = map(int,(input().split(' ')))
if all(1 <= x <= 10**12 for x in [A,B,C]) :
    print(A+B+C)