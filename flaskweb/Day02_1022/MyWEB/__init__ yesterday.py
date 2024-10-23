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


    ### 라우트 기능 함수
    # @Flask Web Server 인스턴스 변수명. route("URL") >>> 무조건 쌍따움표 사욯해야함
    # http://127.0.0.1:5000/
    @APP.route("/")
    def index():
        # return """<body style = 'background-color : skyblue;'>
        #             <h1> Hello </h1>
        #         </body>"""  
        return render_template("index.html")

    # http://127.0.0.1:5000/info
    # http://127.0.0.1:5000/info/
    # '/'가 있는거와 없는거 동시에 만들 수 있다.
    @APP.route("/info")
    @APP.route("/info/")
    def info():
        return """<body style = 'background-color : aqua;'>
                    <h1> INFORMATION </h1>
                </body>"""

    # http://127.0.0.1:5000/info/[문자열변수]
    # name에 문자열 변수 저장, name =  문자열변수
    @APP.route("/info/<name>")
    def printInfo(name):
        # return f"""<body style='background-color:yellow; text=align:center'>
        #         <h1>{name}'s Information</h1>
        #         HELLO!
        #         </body>
        #         """
        return render_template("info.html", name=name)

    # http://127.0.0.1:5000/info/정수
    # age라는 변수에 정수 저장
    @APP.route("/info/<int:age>")
    def Checkage(age):
        return f"""<body style='background-color:pink; text=align:center'>
                <h1>{age}'s Information</h1>
                HELLO! number
                </body>
                """

    # http://127.0.0.1:5000/info/go
    @APP.route("/go")
    def goHome():
        return APP.redirect('/info')

    return APP

### 조건부 실행 >> 아직 라우팅을 하지 않음
if  __name__ =='__main__':
    # Falsk Web Server 구동
    app = create_app()
    app.run()

