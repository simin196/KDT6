import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import seaborn as sns

# 데이터셋 불러오기
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx'
df = pd.read_excel(url)

# 데이터 전처리
df = df[df['Quantity'] > 0]  # 양수만 남김
df = df[df['UnitPrice'] > 0]  # 양수만 남김
df.dropna(subset=['CustomerID'], inplace=True)  # 고객 ID가 없는 행 제거
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']  # 총 구매 금액 계산

import datetime as dt

# 기준 날짜 설정 (데이터 기준 가장 최근 날짜로 설정)
now = df['InvoiceDate'].max() + dt.timedelta(days=1)

# RFM 값 계산
rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (now - x.max()).days,  # Recency
    'InvoiceNo': 'nunique',  # Frequency
    'TotalPrice': 'sum'  # Monetary
}).rename(columns={'InvoiceDate': 'Recency', 'InvoiceNo': 'Frequency', 'TotalPrice': 'Monetary'})

# 데이터 스케일링
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm)

from sklearn.metrics import silhouette_score

# 최적의 클러스터 수 찾기 (Elbow Method)
inertia = []
silhouette_scores = []
cluster_range = range(2, 11)

for k in cluster_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(rfm_scaled)
    inertia.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(rfm_scaled, kmeans.labels_))

# 시각화
fig, ax = plt.subplots(1, 2, figsize=(12, 5))
ax[0].plot(cluster_range, inertia, marker='o')
ax[0].set_title('Elbow Method')
ax[0].set_xlabel('Number of Clusters')
ax[0].set_ylabel('Inertia')

ax[1].plot(cluster_range, silhouette_scores, marker='o')
ax[1].set_title('Silhouette Scores')
ax[1].set_xlabel('Number of Clusters')
ax[1].set_ylabel('Silhouette Score')

plt.show()

# K-means 클러스터링 (클러스터 수는 위 결과에 따라 설정)
optimal_clusters = 4  # 예시로 4개 클러스터 선택
kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
rfm['Cluster'] = kmeans.fit_predict(rfm_scaled)

# 각 클러스터의 특징 분석
cluster_summary = rfm.groupby('Cluster').mean().round(2)
cluster_summary['Customer Count'] = rfm['Cluster'].value_counts()

import ace_tools as tools; tools.display_dataframe_to_user(name="Customer Segmentation Summary", dataframe=cluster_summary)

# 클러스터 별 분포 시각화
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

sns.boxplot(x='Cluster', y='Recency', data=rfm, ax=axes[0])
axes[0].set_title('Recency Distribution by Cluster')

sns.boxplot(x='Cluster', y='Frequency', data=rfm, ax=axes[1])
axes[1].set_title('Frequency Distribution by Cluster')

sns.boxplot(x='Cluster', y='Monetary', data=rfm, ax=axes[2])
axes[2].set_title('Monetary Distribution by Cluster')

plt.show()
