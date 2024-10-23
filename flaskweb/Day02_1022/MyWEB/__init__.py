#------------------------
# flask framework에서 WebServer 구동 파일
# - 파일명 : app,py
#------------------------
### 모듈 로딩
from flask import Flask, render_template

#### 사용자 정의 함수---------------------
def create_app():

    ### 전역 변수 >> 서버 구동 생성
    # Flask Web Server 인스턴스 생성
    APP = Flask(__name__)
   # ^ 이 변수는 마음대로 명명해도됨


    ### 라우트 기능 모듈----------------
    from .views import main_views

    APP.register_blueprint(main_views.main_bp)

    return APP

### 조건부 실행 >> 아직 라우팅을 하지 않음
if  __name__ =='__main__':
    # Falsk Web Server 구동
    app = create_app()
    app.run()

