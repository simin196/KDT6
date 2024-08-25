# 대구시 산격3동의 인구 분포 그래프 그리기

import csv
import re
import matplotlib.pyplot as plt
import koreanize_matplotlib

f= open('age.csv', encoding='euc_kr')
data= csv.reader(f)  
header = next(data)

result=[]
city=''

for row in data:
    if '산격3동' in row[0]:
        str_list= re.split('[()]', row[0]) # 정규식(re): 여러 구분자 사용 가능 위같이 import해야함
        city= str_list[0]                  # row[0]: '대구광역시 북구 산격3동(2723063000)'
        
        # 0세 부터 100세 이상까지 데이터
        for data in row[3:]:
            data= data.replace(',','') # 천 단위 콤마 삭제 
            result.append(int(data)) # 문자열을 숫자로 변환
f.close()
print(result)

plt.title(f'{city} 인구현황')
plt.xlabel('나이')
plt.ylabel('인구수')
plt.plot(result)
plt.show()

