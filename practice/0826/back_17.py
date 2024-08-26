# 1에서부터 6까지의 눈을 가진 3개의 주사위
'''
같은 눈이 3개가 나오면 10,000원+(같은 눈)*1,000원
같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)*100원
모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)*100원
'''
# set이용하는 방법도있지 않을까?

a,b,c = map(int,(input().strip().split(' ')))

if 1<=a<=6 and 1<=b<=6 and 1<=c<=6:
    if a==b and a==c and c==b: 
        print(10000+(1000*a))
    
    elif (a==b and a==b) or (b==a and b==c) or (c==a and c==b):
        if a==b and a==b:
            print(1000+(100*a))
        elif b==a and b==c:
            print(1000+(100*b))
        else: 
            print(1000+(100*c))

    else:
        point =  0
        p = [a,b,c]
        for i in p:
            if i > point:
                point = i
        print((100*point))  