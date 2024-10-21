# 모듈 로딩--------------------------------------------
import os.path     # 파일 및 폴더 관련
import cgi, cgitb  # cgi 프로그래밍 관련
import joblib      # AI 모델 관련
import sys, codecs # 인코딩 관련
import torch
import numpy as np 
from pydoc import html
from PIL import Image
from torchvision import transforms
import io
import torch.nn as nn
import torch.nn.functional as F
import base64

    
# 동작관련 전역 변수----------------------------------
SCRIPT_MODE = True    # Jupyter Mode : False, WEB Mode : True
cgitb.enable()         # Web상에서 진행상태 메시지를 콘솔에서 확인할수 있도록 하는 기능

def showHTML(text, msg, img_data=""):
    print("Content-Type: text/html; charset=utf-8")
    print(f"""
    <!DOCTYPE html>
    <html lang="en">
     <head>
      <meta charset="UTF-8">
      <title>---NAVER Shopping review---</title>
      <style>
        .container {{
            margin-top: 20px;
        }}
        #preview {{
            margin-top: 20px;
            max-width: 100%;
            height: auto;
        }}
      </style>
     </head>
     <body>
      <div class="container">
        <form enctype="multipart/form-data" method="post">
          <p>이미지 업로드: <input type="file" id="imageInput" name="image" accept="image/*" /></p>
          <img id="preview" src="data:image/png;base64,{img_data}" alt="이미지 미리보기">
          <p><input type="submit" value="예측"></p>
          <p>{msg}</p>
        </form>
      </div>

      <script>
        // 이미지 미리보기 기능
        document.getElementById('imageInput').addEventListener('change', function(event) {{
            const file = event.target.files[0];
            const reader = new FileReader();

            reader.onload = function(e) {{
                document.getElementById('preview').src = e.target.result;
            }};

            if (file) {{
                reader.readAsDataURL(file);  // 이미지를 읽어서 미리보기로 표시
            }}
        }});
      </script>
     </body>
    </html>""")

# 사용자 입력 데이터를 예측하는 함수-----------------------------------------------------------
def detectRANK(text_field, model):
    if text_field is None or text_field.filename == "":
        return "이미지가 업로드되지 않았습니다.", ""

    # 파일 전처리
    text_data = text_field.file.read()
    
    # 텐서화 변환
    image_tensor = data_transform(image).unsqueeze(0)

    # 모델 예측
    model.eval()
    with torch.no_grad():
        output = model(image_tensor)
        # 예측 결과 확인
        _, predicted = torch.max(output, 1)

    class_names = ['가짜', '진짜']
    
    return class_names[predicted], img_str


# (1) WEB 인코딩 설정
if SCRIPT_MODE:
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach()) 

# (2) 모델 로딩
if SCRIPT_MODE:
    pklfile = os.path.dirname(__file__)+ 'C:\Users\KDP-23\Desktop\KDT6\NLP\project\model\best_model\best_model4.pth' 
else:
    pklfile = 'C:\Users\KDP-23\Desktop\KDT6\NLP\project\model\best_model\best_model4.pth'

model= torch.load(pklfile, map_location=torch.device('cpu'), weights_only=False)

# (3) WEB 사용자 입력 데이터 처리
# (3-1) HTML 코드에서 사용자 입력 받는 form 태크 영역 객체 가져오기
form = cgi.FieldStorage()

# (3-2) Form에서 이미지 데이터 가져오기
image_field = form.getfirst("image", None)

# (3-3) 예측하기
if image_field and "image" in form and form["image"].filename:
    result, img_data = detectRANK(form["image"], model)
    msg = f"예측 결과: {result}"
else:
    msg = "이미지가 업로드되지 않았습니다."
    img_data = ""

# (4) 사용자에게 WEB 화면 제공
showHTML("", msg, img_data)
