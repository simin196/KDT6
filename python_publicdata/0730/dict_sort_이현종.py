data={'Seoul':['South Korea','Asia',9655000],
      'Tokyo':['Japan','Asia',14110000],
      'Beijing':['China','Asia',21540000],  
      'London':['United Kingdom','Europe',14800000],    
      'Berlin':['Germany','Europe',3426000],  
      'Mexico City':['Mexico','America',21200000]}   




while True:
    print('''
    -----------------------------------------
    1.	전체 데이터 출력		
    2.	수도 이름 오름차순 출력											
    3.	모든 도시의 인구수 내림차순 출력		
    4.	특정 도시의 정보 출력		
    5.	대륙별 인구수 계산 및 출력		
    6.	프로그램 종료
    -----------------------------------------
    ''')
    a=input('메뉴를 입력하세요:	')
    
    if a == '1':  
        for i in range(6):
            print(f'[{i+1}] {list(data.keys())[i]}: {list(data.values())[i]}')
    
    elif a == '2':
        b = list(data.keys())
        key1=sorted(b)
        for i in range(6):
            print(f'[{i+1}] {key1[i]}: {list(data.values())[i]}')
    
    elif a == '3':
        data3 = sorted(data.items(), key=lambda item: item[1][2], reverse=True)
        population= len(f"{data3[0][1][2]:,}")
        for i in range(6):
            key, value = data3[i]
            print(f"[{i + 1}] {key:15}: {value[2]:>{population},}")
    
    elif a == '4':
        city = input("출력할 도시 이름을 입력하세요: ")
        if city in data:
            value = data[city]
            print(f"도시:{city}\n국가:{value[0]}, 대륙:{value[1]}, 인구수:{value[2]:,}")
        else:
            print(f"도시이름: {city}은 key에 없습니다.")
    
    elif a == '5':
        continent = input("대륙 이름을 입력하세요(Asia, Europe, America): ")
        total_population = 0
        for key in data:
            value = data[key]
            if value[1] == continent:
                print(f"{key}: {value[2]:,}")
                total_population += value[2]
        print(f"{continent} 전체 인구수: {total_population:,}")
    
    elif a == '6':
        print("프로그램을 종료합니다.")
        break
    
    else:
        print("잘못된 입력입니다. 다시 시도하세요.")
        

