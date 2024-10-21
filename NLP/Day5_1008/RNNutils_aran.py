import re
from collections import Counter
import numpy as np
import torch
import os

with open('basic_ko_stopwords_aran.txt') as f:
    stop_words=f.read().split('\n')


def getToken(textlist,tokenizer):
    """한글만 남기고 불용어 제거 및 토큰화"""
    text_to_token=[]
    for idx,text in enumerate(textlist):
        # 한글빼고 다지우기 [정규식]
        text=re.sub('[^ㄱ-ㅎ가-힣]+',' ',text)

        # 토큰으로 변환 [norm,stem << 참고] 
        tokens=tokenizer.morphs(text,norm=True)
        for token in tokens:
            # 불용어 목록에 있는 단어 토큰 제거
            if token in stop_words:
                tokens.remove(token)
        text_to_token.append(tokens)

    return text_to_token # 문장 토큰화


def get_vocab(text_to_token, n_vocab):
    """단어 사전 생성: n_vocab 갯수만큼 자주 사용된 단어들을 포함"""    
    # text_to_token 내의 모든 토큰을 하나의 리스트로 만듦
    tokenlist = [token for token in text_to_token]
    
    # 단어의 출현 빈도를 기록할 Counter 객체 생성
    counter = Counter()
    
    # 각 토큰 리스트에 대해 빈도수 업데이트
    for tokens in tokenlist:
        # Counter 객체에 토큰 리스트를 전달해 빈도수를 업데이트
        counter.update(tokens)
    
    # 단어 사전의 시작 부분에 패딩('<pad>')과 사전에 없는 단어('<oov>')를 추가
    vocab = ['<pad>', '<oov>']
    
    # 가장 자주 등장하는 n_vocab개의 단어를 vocab에 추가
    for token, count in counter.most_common(n_vocab):
        vocab.append(token)
    
    # 생성된 단어 사전을 반환
    return vocab


def padding_vectorize(tokenlist, token_to_idx, pad_length):
    """ 토큰 리스트를 패딩 길이에 맞추고, 수치화 """
    
    # 수치화된 결과(인덱스 리스트)를 저장할 리스트
    idxlist = []
    
    # OOV (Out Of Vocabulary: 사전에 없는 단어) 토큰의 인덱스 값을 가져옴
    oov_num = token_to_idx['<oov>']
    
    # tokenlist에 있는 각 토큰 리스트에 대해 반복
    for tokens in tokenlist:
        # 토큰 길이가 pad_length보다 크거나 같으면 자름
        if len(tokens) >= pad_length:
            tokens = tokens[:pad_length]
        # 토큰 길이가 pad_length보다 짧으면 '<pad>'로 패딩
        else:
            tokens = tokens + (['<pad>'] * (pad_length - len(tokens)))
        
        ## 각 토큰을 token_to_idx 사전에서 해당 인덱스로 변환
        # 사전에 없는 토큰은 OOV 토큰의 인덱스로 변환
        numbers = [token_to_idx.get(token, oov_num) for token in tokens]
        
        # 변환된 인덱스 리스트를 idxlist에 추가
        idxlist.append(numbers)
    
    # 결과 리스트를 numpy 배열로 변환하여 반환
    return np.array(idxlist)

        
from torch import nn

class SentenceClassifier(nn.Module):
    def __init__(
            self,
            n_vocab,
            hidden_dim,
            embedding_dim,
            n_layers,
            feature_n,
            dropout=0.5,
            bidirectional=True,
            model_type='lstm'
            ):
        super().__init__()

        self.embedding=nn.Embedding(
            num_embeddings=n_vocab,
            embedding_dim=embedding_dim,
            padding_idx=0
        )
        if model_type=='rnn':
            self.model=nn.RNN(
                input_size=embedding_dim,
                hidden_size=hidden_dim,
                num_layers=n_layers,
                bidirectional=bidirectional,
                dropout=dropout,
                batch_first=True
            )
        elif model_type=='lstm':
            self.model=nn.LSTM(
                input_size=embedding_dim,
                hidden_size=hidden_dim,
                num_layers=n_layers,
                bidirectional=bidirectional,
                dropout=dropout,
                batch_first=True   
            )
        
        if bidirectional:
            self.classifier=nn.Linear(hidden_dim*2,feature_n)
        else:
            self.classifier=nn.Linear(hidden_dim,feature_n)
        self.dropout=nn.Dropout(dropout)

    def forward(self,inputs):
        embeddings=self.embedding(inputs)
        output,_=self.model(embeddings)
        last_output=output[:,-1,:]
        last_output=self.dropout(last_output)
        logits=self.classifier(last_output)
        return logits
    
class Train_val():
    def __init__ (self,trainDL,valDL,model,optimizer,lossF,scoreF):
        self.trainDL=trainDL
        self.valDL=valDL
        self.model=model
        self.lossF=lossF
        self.scoreF=scoreF
        self.optimizer=optimizer
    
    def train(self,EPOCH,scheduler,modelnum):
        HISTORY={'loss':[[],[]],'score':[[],[]]}

        self.model.train()
        for epoch in range(EPOCH):

            loss_total=0
            score_total=0

            for feature,target in self.trainDL:
                pre_y=self.model(feature)
                loss=self.lossF(pre_y,target.reshape(-1).long())
                score=self.scoreF(pre_y,target.reshape(-1))

                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()

                loss_total+=loss.item()
                score_total+=score.item()

            HISTORY['loss'][0].append(loss_total/len(self.trainDL))
            HISTORY['score'][0].append(score_total/len(self.trainDL))

            self.model.eval()
            with torch.no_grad():
                for feature,target in self.valDL:
                    val_pre_y=self.model(feature)

                    loss=self.lossF(val_pre_y,target.reshape(-1).long())
                    score=self.scoreF(val_pre_y,target.reshape(-1))
                
                HISTORY['loss'][1].append(loss.item())
                HISTORY['score'][1].append(score.item())
            

            # 모델 폴더가 없다면 생성
            if not os.path.exists('model/'):
                os.mkdir('model/')


            # test score가 최고 인점 저장
            if len(HISTORY['score'][1])==1:
                torch.save(self.model,f'model/best_model{modelnum}.pth')
                #torch.save(self.model.state_dict(),f'model/best_weight{modelnum}.pth')
        
            elif HISTORY['score'][1][-1]>=min(HISTORY['score'][1]):
                torch.save(self.model,f'model/best_model{modelnum}.pth')
                #torch.save(self.model.state_dict(),f'model/best_weight{modelnum}.pth')

                
            print(f'[{epoch+1}/{EPOCH}]')
            print(f"train loss {HISTORY['loss'][0][-1]}, train score {HISTORY['score'][0][-1]}")
            print(f"val loss {HISTORY['loss'][1][-1]}, val score {HISTORY['score'][1][-1]}")

            # test score 기준으로  scheduler 생성

            scheduler.step(HISTORY['score'][1][-1])
            print(f'scheduler.num_bad_epochs { scheduler.num_bad_epochs}/{ scheduler.patience}')

            if scheduler.num_bad_epochs >= scheduler.patience:
                print(f'[{scheduler.patience}] EPOCH 성능개선이 없어서 조기 종료함')
                break

        return HISTORY
