#------------------------
# flask framework에서 모듈단위 URL 처리 파일
# - 파일명 : main_view.py
#------------------------
### 모듈 로딩
from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect
from DBWEB.models.model import Question

### Blueprint 인스턴스 생성
mainBP = Blueprint('MAIN',
                   import_name=__name__,
                   url_prefix='/')
                #  template_folder='templates')
                                                                                                                                                                                                                                                                                                                                                                                                                        
@mainBP.route('/')
def index():
    return redirect(url_for('question._list'))


    # question_list = Question.query.order_by(Question.create_date.desc())
    # return render_template('question_list.html',
    #                        question_list=question_list)


# # http://localhost:5000/question_list URL 처리 라우딩 함수 정의
# @mainBP.route("/")
# def printList():
#     ## DB에서 조회한 결과를 HTML 파일로 전달
#     q_list = Question.query.all()
#     return render_template('question_list.html', question_list=q_list)


# ### 상세 조회
# # # http://localhost:5000/qedtail/<int:id> URL 처리 라우딩 함수 정의
@mainBP.route("/detail/<int:question_id>/")
def detail(question_id):
    ## DB에서 조회한 1개의 question 인스턴스를 전달
    q=Question.query.get_or_404(question_id)
    return render_template('question_detail.html', question=q)
 