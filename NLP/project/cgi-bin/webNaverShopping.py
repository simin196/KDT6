# 모듈 로딩--------------------------------------------
import os.path     # 파일 및 폴더 관련
import cgi, cgitb  # cgi 프로그래밍 관련
import joblib      # AI 모델 관련
import sys, codecs # 인코딩 관련
import torch
import numpy as np 
import base64

# 텍스트 전처리를 위한 라이브러리 추가
from konlpy.tag import Okt

# 동작관련 전역 변수----------------------------------
SCRIPT_MODE = True    # Jupyter Mode : False, WEB Mode : True
cgitb.enable()         # Web상에서 진행상태 메시지를 콘솔에서 확인할수 있도록 하는 기능

# 텍스트 전처리 함수
import re
stop_words = 'basic_ko_stopwords.txt'

MODEL_FILE = 'best_model4.pth'
VOCAB_FILE = 'vocab.txt'
STOPWORD_FILE = 'basic_ko_stopwords.txt'
max_length = 50

# 모델 로드
def load_model(MODEL_FILE):
   if os.path.exists(MODEL_FILE):
      model = torch.load(MODEL_FILE)
      return model

   else:
      result = '파일이 없습니다.'
      return result

# 한글만 토큰화
def getToken(textlist,tokenizer):
    text_to_token=[]
    for idx,text in enumerate(textlist):
        # 한글빼고 다지우기
        text=re.sub('[^ㄱ-ㅎ가-힣]+',' ',text)

        # 토큰 추출
        tokens=tokenizer.morphs(text,norm=False, stem=False)
        for token in tokens:
            # stop word 체크
             if token in stop_words:
                  tokens.remove(token)
        text_to_token.append(tokens)

    return text_to_token

## 패딩
def pad_sequences(sequences, max_length, pad_value):
    result = list()
    for sequence in sequences:
        sequence = sequence[:max_length]
        pad_length = max_length - len(sequence)
        padded_sequence = sequence +[pad_value] * pad_length
        result.append(padded_sequence)
    return np.asarray(result)

def showHTML(msg):
    print("Content-Type: text/html; charset=utf-8")
    print(f"""
    <!DOCTYPE html>
    <html lang="en">
     <head>
      <meta charset="UTF-8">
      <title>---NAVER Shopping review---</title>
     </head>
     <body>
      <div class="container">
        <form method="post">
          <p>리뷰 입력: <textarea name="review" rows="4" cols="50"></textarea></p>
          <p><input type="submit" value="예측"></p>
          <p>{msg}</p>
        </form>
      </div>
     </body>
    </html>""")

# 사용자 입력 데이터를 예측하는 함수-----------------------------------------------------------
def detectRANK(text_field, model):
    if text_field is None or text_field == "":
        return "리뷰가 입력되지 않았습니다."

    # 텍스트 전처리
    tokenizer = Okt()
    text_tokens = [ token for token in tokenizer.morphs(text_field, norm=False, stem=False)]
    print(text_tokens)

    # 단어사전 불러오기
    with open(VOCAB_FILE, 'r', encoding='utf-8') as f:
        vocab = f.readlines()
        id_to_token ={idx: token.replace('\n','') for idx, token in enumerate(vocab)}
        print(id_to_token)

    key_unk = [key for key, value in id_to_token.items() if value == '<unk>']
    unk_id = key_unk[0]

    text_ids = [
    [id_to_token.get(token, unk_id) for token in review] for review in text_tokens]

    key_pad = [key for key, value in id_to_token.items() if value == '<pad>']
    pad_id = key_pad[0]

    text_ids = pad_sequences(text_ids, max_length, pad_id)

    text_ids = torch.tensor(text_ids)

    mymodel = load_model(MODEL_FILE)

    # 예측을 위해 모델에 입력
    mymodel.eval()

    with torch.no_grad():
    
        # 예측
        pre_y = mymodel(text_ids)
        yhat = torch.sigmoid(pre_y)>.5

        # 결과 출력 (임계값을 0.5로 설정해 긍정/부정 분류)
        if yhat.all():  
            result = "긍정"
        else:
            result = "부정"
        
    print(result)
        
        

# (1) WEB 인코딩 설정
if SCRIPT_MODE:
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach()) 

# (2) 모델 로딩
if SCRIPT_MODE:
    pklfile = os.path.join(os.path.dirname(__file__), 'C:\\Users\\KDP-23\\Desktop\\KDT6\\NLP\\project\\model\\best_model\\best_model4.pth') 
else:
    pklfile = 'C:\\Users\\KDP-23\\Desktop\\KDT6\\NLP\\project\\model\\best_model\\best_model4.pth'

model = torch.load(pklfile, map_location=torch.device('cpu'))

# (3) WEB 사용자 입력 데이터 처리
# (3-1) HTML 코드에서 사용자 입력 받는 form 태크 영역 객체 가져오기
form = cgi.FieldStorage()

# (3-2) Form에서 리뷰 데이터 가져오기
review_field = form.getfirst("review", None)

# (3-3) 예측하기
if review_field:
    msg = detectRANK(review_field, model)
else:
    msg = "리뷰가 입력되지 않았습니다."

# (4) 사용자에게 WEB 화면 제공
showHTML(msg)
