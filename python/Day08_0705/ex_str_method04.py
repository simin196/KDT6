#--------------------------------------------------------------------------
# 문자열 전용의 함수 즉. 메서드(Method)
#--------------------------------------------------------------------------

## 문자열에서 원소/요소 변경해주는 매서드 => replace()
msg='Pithon'

# 인덱스로 요소 변경 >>>> ERROR 미지원 기능: 불변의 시퀀스 타입
# msg[1]='y'

# 전용 메서드로 변경
m1 = msg.replace('i','y')
print(f'msg : {msg} -----------> m1 : {m1}')

# 변경 적용 위해서는 반드시 저장!!
msg= msg.replace('i','y')
print(f'msg : {msg} -----------> m1 : {m1}')

msg='Good Happy'
# - o --> O로 변경 # 해당하는 문자를 모두 다 수정한다.
print(msg.replace('o','O'))

# if 하나만 수정하고 싶다면
print(msg.replace('o','O', 1))

## 1개의 문자열을 여러개 문자열로 분리해주는 메서드 split()
# - 분리기준 => 기본값 : (공백)
msg=' Happy New Year '

result= msg.split()
print(result)

phone='오늘은 날씨가 좋군요. 내일도 날씨가 좋을까요?'
result=phone.split('. ')
print(f'result = > {result}, {type(result)}')

## 여러개 문자열을 1개 문자열로 합쳐주는 메서드 join()
# - 합칠문자.join(여러개 문자열)
# -> 010*2222*3333 
con=['010','2222','3333']
phone=' * '.join(con)
print(phone)