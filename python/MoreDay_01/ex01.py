# 1. ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다.
#    화면에 종가데이터를 출력하라.

ohlc = [["open", "high", "low", "close"], #>>>>>>>>>>>>>>중복 list
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

# # 출력 결과:
# #  100
# #  190
# #  310

# 1. ohlc 묶여있는 리스트를 풀어주고 >>> 안에 list하나하나를 a, b, c, d로 생각
# 2. 각 리스트에 인덱스[-1]자리를 
# 3. 반복문으로 써서 나열하는데 숫자만 

for data in ohlc:
    print(data[3])
    



#----------------------------------------------------------------------------------------------------------------------
#2. 주민등록번호 뒷 자리 7자리 중 첫째 자리는 성별을 나타내는데, 1, 3은 남자 2, 4는 여자를 의미한다.
#   사용자로부터 13자리의 주민등록번호를 입력 받은 후 성별 (남자, 여자)를 출력하는 프로그램을 작성하라.

# 입력 : 821010-1635210

# # 출력 : 남자
# print()
jumin = 821010-1635210

if int(jumin[7])==1 or int(jumin[7])==3:
    print('남자')
else :
    print('여자')

    
if jumin[7]=='1' or jumin[7]=='3':
    print('남자')
else :
    print('여자')

