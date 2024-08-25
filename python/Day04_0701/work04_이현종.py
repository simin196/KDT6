#[12.4]
camille={
'health':575.6,
'health_regen':1.7,
'mana': 338.8,
'mana_regen':1.3,
'melmm':125,
'attack_damage':60,
'attack_speed':0.625,
'armor':26,
'magic_resistance':32.1,
'movement_speed':340}

print(camille['health'])
print(camille['movement_speed'])

#[12.5]
data=['health','mana', 'melmm','attack_speed', 'magic_resistance']
num=[575, 308.8, 600, 0.625, 35.7]
print(dict(zip(data,num)))

#[13.6]
x=5
if x != 10 :
    print('ok')


#[13.7]
price=input('가격을 적으시오 : ')
sell=input('사용할 쿠폰을 적으시오 : ')

if sell in 'Cash3000' :
    print(f' {int(price)-3000}')
if sell in 'Cash5000' :
    print(f' {int(price)-5000}')

#[14.6]

written_test=75
coding_test=True

if written_test>=80 and coding_test==True:
    print('합격')
else:
    print('불합격')

#[14.7]
jumsu=input('점수를 입력하세요').split(' ')
# print(0<=int(nums[0])<=100)
# print(int(nums[0]) in range(101))
n1=list(map(int, jumsu))
if 0<= n1[0] <=100 and 0<= n1[1] <=100 and 0<= n1[2] <=100 and 0<= n1[3] <=100  :
    jumsu1=(int(jumsu[0])+int(jumsu[1])+int(jumsu[2])+int(jumsu[3]))/4  #sum()으로도 가능하다.
    print(jumsu1, type(jumsu1))
    if jumsu1>=80:
        print('합격')
    else :
        print('불합격')
else:
    print('잘못된 점수')

#[15.3]
x=int(input())

if 11<= x <=20:
    print('11~20')
elif 21<= x <=30:
    print('21~30')
else :
    print('아무것도 해당되지 않습니다.')

#[15.4]

age=int(input())
balance=9000
if age<=6:
    balance=balance-0
elif 7<=age<=12:
    balance=balance-650
elif 13<=age<=18:
    balance=balance-1050
else :
    balance=balance-1250

print(balance)