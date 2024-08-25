import requests
from bs4 import BeautifulSoup

# 페이지 URL
url = "https://www.saramin.co.kr/zf_user/jobs/list/job-category?page=7&cat_kewd=2248%2C82%2C83%2C109%2C116%2C107%2C106&search_optional_item=n&search_done=y&panel_count=y&preview=y&isAjaxRequest=0&page_count=100&sort=RL&type=job-category&is_param=1&isSearchResultEmpty=1&isSectionHome=0&searchParamCount=1&tab=job-category#searchTitle"

# 페이지 HTML 가져오기
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 키워드 추출 (예를 들어, 'span' 태그와 특정 클래스명을 사용하여 추출)
keywords = []

for element in soup.find_all('span', class_='keyword_class_name'):
    keywords += element.get_text().split(',')

# 중복 제거 및 리스트 정리
keywords = [keyword.strip() for keyword in keywords if keyword.strip()]

print(keywords)
