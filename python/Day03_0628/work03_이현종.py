#[9.3]
s='''Python is a programming language that lets you work quickly
and
integrate systems more effectively.'''
print(s)

#[9.4]
s='''\'Python\' is a "programming language"
that lets you work quickly
and
integrate systems more effectively.'''
print(s)

#[10.4]
a= range(5,-10,-2)
print(list(a))

#[10.5]
a=input('정수를 입력하세요 : ')
b=range(-10,10,int(a))
print(list(b))

#[11.6]
year= [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
population= [1024979, 10195318, 1014345, 10103233, 10022181, 9930616, 9857426, 9838892]

print(year[-3:])
print(population[-3:])

#[11.7]
n=-32, 75, 97, -10, 9, 32, 4, -15, 0, 76, 14, 2 
print(n[1::2])

#[11.8]
a=input('데이터를 입력하세요 : ').split()
del a[-4:]
print(a)

#[11.9]
a= input('첫번째 데이터를 입력하세요 : ')
b= input('두번째 데이터를 입력하세요 : ')
print(a[1::2]+b[0::2])