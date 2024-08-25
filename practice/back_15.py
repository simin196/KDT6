H,M = map(int,(input().split(' ')))
if 0 <= H <= 23 and 0 <= M <= 59:
    M1 = M-45
    if M1 < 0 :
        H = H-1
        M1 = 60 + M -45

        if H < 0: 
            H = 23
            print(H, M1, sep=' ')
        else:
            print(H, M1, sep=' ')
    else:
        print(H, M1, sep=' ')
