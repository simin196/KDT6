#[5.5]
m=input('도로와의 거리를 적으시오(m 단위로) : ')
m=int(m)
print(int(0.2467*m+4.159))

#[5.6]
AP=input('현재 캐릭터의 AP를 적으시오: ')
ap=int(AP)
print(ap * 0.6 +225)

#[6.6]
num = input('정수 3개를 띄어쓰시오 : ')
num=num.split()
print(int(num[0])+int(num[1])+int(num[2]))

#[6.7]
a, b, c = 50, 100, 'None'
print(a)
print(b)
print(c)

#[6.8]
kor=input('국어 : ')
eng=input('영어 : ')
math=input('수학 : ')
sci=input('과학 : ')

a=int(kor)
b=int(eng)
c=int(math)
d=int(sci)

print(int((a+b+c+d)/4))

#[7.4]
year=2000
month=10
day=38
hour=11
min=43
sec=59

print(year, month, day, sep='/', end=' ')
print(hour, min, sec, sep=':')

#[7.5]
year, month, day, hour, min, sec = input().split()

print(year, month, day, sep='-', end='T')
print(hour, min, day, sep=':')

#[8.4]
kor=92
eng=47
math=86
sci=81

print(kor>=50 and eng>=50 and math>=50 and sci>=50)

[8.5]

kor=input('국어 : ')
eng=input('영어 : ')
math=input('수학 : ')
sci=input('과학 : ')

print(int(kor)>=90 and int(eng)>80 and int(math)>85 and int(sci)>=80)