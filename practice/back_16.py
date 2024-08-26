A,B = map(int,(input().split(' ')))
if 0 <= A <= 23 and 0 <= B <= 59:

    C = int(input())
    if 0 <= C <= 1000:
        C1 = C//60
        C2 = C%60 
        B1 = B+C2
        A1 = A+C1

        if B1 >= 60:
            B1 = (B+C2) - 60
            A1 = A + C1 + 1

            while True:
                
                if A1 >= 24:
                    A1 = A1-24
                else:
                    print(f'{A1} {B1}')
                    break
        else:
            print(f'{A1} {B1}')
    