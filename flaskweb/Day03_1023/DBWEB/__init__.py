#------------------------
# flask framework에서 WebServer 구동 파일
# - 파일명 : app,py
#------------------------
### 모듈 로딩
from flask import Flask, render_template

# DB관련 설정
import config
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
                             # SQLAlchemy > 야는 어떤DB든 간에 다 불러올수있다     

DB= SQLAlchemy()
MIGRATE = Migrate()

#-------------------------------------------
# Application 생성 함수
# 함수명 : create_app <== 이름 변경 불가!!!
#-------------------------------------------
def create_app():
    # Flask Web Server 인스턴스 생성
    APP = Flask(__name__)

    # DB 관련 초기화 설정
    APP.config.from_object(config)

    # DB 초기화 및 연동
    DB.init_app(APP)
    MIGRATE.init_app(APP, DB)

    # DB클래스 정의 모듈 로딩
    from .models import model 

    # URL 처리 모듈 등록
    from .views import main_view, question_views, answer_views
    APP.register_blueprint(main_view.mainBP)
    APP.register_blueprint(question_views.bp)
    APP.register_blueprint(answer_views.bp)

    return APP
