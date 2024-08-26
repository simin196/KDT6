a = int(input())
if 1<=a<=4000:
    if a%4==0:
        if a%100 == 0 :
            if int(a)%400 == 0:
                print(1)
            else:
                print(0)
        else:
            print(1)
    else:
        print(0)
