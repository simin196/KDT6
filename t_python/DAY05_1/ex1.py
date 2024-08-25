
dan=int(input("단 입력(2~9):"))

if dan in range(2, 10):
    for n in range(1,10):
        print(f'{dan}*{n}={dan*n}')
else: 
    print("구구단은 2단부터 9단까지입니다.")
