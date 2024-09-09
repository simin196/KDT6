#### ML Process

'''
1. 데이터 처리 >>> 데이터 로딩 , 데이터 확인 (실제 데이터 확인 및 탐색)

2. 데이터 전처리 >> info() 정보 , descrive() 분포, unqiue , 
    >>> 정제(결측치, 중복값, 이상치, 컬럼 고유값...)
    >>> 피쳐에 대한 처리(인코디으 스케일링...)
    >>> 피쳐 선택 및 가공
    >>> 피쳐와 타겟(독립변수와 종속변수)

3. 학습준비
    >>> 데이터셋 (train, validation(검증), test)
        >>> 데이터가 부족 및 일반화 위해서 train, test데이터 셋 분리

4. 학습진행
    >>> 교차검증으로 학습 진행 : train 데이터셋 사용

5. 모델 평가
    >>> test 데이터셋(DS)으로 평가
    >>> 평가기준 : 분류와 회귀가 다름 

--------------------------------------- 여기까지 1차

# 추가적으로

### 모델의 성능을 높이는 작업 >> 튜닝 진행
- Hyper parameter 제어 : 모델 인스턴스 생성 시 매개변수로 설정
- 새로운 모델로 학습 진행 --> 평가

'''