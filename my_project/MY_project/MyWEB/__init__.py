### 모듈 로딩
from flask import Flask, render_template

#### 사용자 정의 함수---------------------
def create_app():

    ### 전역 변수 
    # Flask Web Server 인스턴스 생성
    APP = Flask(__name__)

    ### 라우트 기능 함수
    # @Flask Web Server 인스턴스 변수명. route("URL") >>> 무조건 쌍따움표 사욯해야함

    ## home
    @APP.route("/")
    def index(): 
        return render_template("index.html")

    ## ML
    @APP.route("/ml")
    @APP.route("/ml/")
    def index_ml():
        return render_template("index_ml.html")


    ## DL
    @APP.route("/dl")
    @APP.route("/dl/")
    def index_dl(): 
        return render_template("index_dl.html")


    ## CV
    @APP.route("/cv")
    @APP.route("/cv/")
    def index_cv(): 
        return render_template("index_cv.html")



    ## NLP
    @APP.route("/nlp")
    @APP.route("/nlp/")
    def index_nlp(): 
        return render_template("index_nlp.html")

    
    return APP

### 조건부 실행 >> 아직 라우팅을 하지 않음
if  __name__ =='__main__':
    # Falsk Web Server 구동
    app = create_app()
    app.run()

