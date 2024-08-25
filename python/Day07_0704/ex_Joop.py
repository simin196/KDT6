##[1] outer = 5 , inner = 5
for i in range(5):
    for j in range(5):
        print(f'j:{j}', end=' ')
    print(f'i:{i}\\n')


# 대각선 * 출력
# *
#  *
#   *
#    *
#     * 으로 출력 
for v in range(5):
    for h in range(v+1):
        # if h==v: 방법 1번
        #     print('*')
        # else:
        #     print(' ',end="") 
        print( '*' if h==v else ' ',end='\n' if h==v else '') # 방법 2번


