import os
import sys
import urllib.request
client_id = "ChiGUKS2z5TaNLK4HW5I"
client_secret = "5pWxfxIehS"
encText = urllib.parse.quote("빅데이터")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)

'''
"items":[
                {
                        "title":"<b>빅데이터<\/b>분석기사 자격증 학점은행제로 준비
했어요",
                        "link":"https:\/\/blog.naver.com\/likesonny\/223517449088",
                        "description":"사회는 <b>빅데이터<\/b>가 무시할 수 없는 중
요성을 갖고 있는데요 그만큼 인기도 높아지고 수요도 늘어나서 전망이 매우 좋다고 느끼게 되었죠 보면 볼수록 메리트가 많은 것 같아서 저도 <b>빅데이터<\/b>분석기사 자격증
을... ",
                        "bloggername":"진상의 추억",
                        "bloggerlink":"blog.naver.com\/likesonny",
                        "postdate":"20240719"
'''