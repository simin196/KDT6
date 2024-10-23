#------------------------
# flask framework에서 '/'URL에 대한 라우팅 처리 파일
# - 파일명 : main_views.py
#------------------------
### 모듈 로딩
from flask import Blueprint, render_template

# Blueprint()
main_bp = Blueprint('main',
                     __name__,
                     url_prefix='/',
                     template_folder='templates')

# 라우팅 기능 함수 정의
# 자동으로 http://127.0.0.1:5000/ 은 저장됨
@main_bp.route('/', endpoint= 'hello')
def index():
    return render_template('index.html')

# 엔드포인트 > 해당 함수의 별칭
# 엔드포인트는 안바꾸는데
# 함수는 변경할수도있다
# >> 난중에 의사 소통할때 수월히 할수있다. 
# 함수이름이 외부로 노출되지 않는다
# 