import torch
from flask import Flask, request, render_template
from torch.nn import functional as F
from transformers import BertTokenizer  # Assuming a tokenizer is needed for text preprocessing
from torch import nn

app = Flask(__name__)

# Load your model (assuming it’s a binary classification model)
class SentenceClassifier(nn.Module):
    def __init__(self,
                 n_vocab,
                 hidden_dim,
                 embedding_dim,
                 n_layers, 
                 dropout = 0.5,
                 bidirectional = True,
                 model_type = 'lstm'):
        super().__init__()

        self.embedding = nn.Embedding(
            num_embeddings=n_vocab,
            embedding_dim=embedding_dim,
            padding_idx=0)
        
        if model_type == 'rnn':
            self.model = nn.RNN(
                input_size=embedding_dim,
                hidden_size=hidden_dim,
                num_layers=n_layers,
                bidirectional=bidirectional,
                dropout=dropout,
                batch_first=True)
    
        elif model_type == 'lstm':
            self.model = nn.LSTM(
                input_size=embedding_dim,
                hidden_size=hidden_dim,
                num_layers=n_layers,
                bidirectional=bidirectional,
                dropout=dropout,
                batch_first=True)
            
        if bidirectional:
            self.classifier = nn.Linear(hidden_dim * 2, 1)
        else:
            self.classifier = nn.Linear(hidden_dim, 1)
        
        self.dropout = nn.Dropout(dropout)

    def forward(self, inputs):
        embeddings = self.embedding(inputs)
        output, _ = self.model(embeddings)
        last_output = output[:, -1, :]
        last_output = self.dropout(last_output)
        logits = self.classifier(last_output)
        return logits

# Initialize the model with the required parameters
n_vocab = 10002
hidden_dim = 128  # Example, adjust based on your needs
embedding_dim = 300  # Example, adjust based on your model
n_layers = 2  # Example, adjust based on your architecture

model = SentenceClassifier(n_vocab=n_vocab, hidden_dim=hidden_dim, embedding_dim=embedding_dim, n_layers=n_layers)
model.load_state_dict(torch.load('best_model4.pth', map_location=torch.device('cpu')))
model.eval()

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    review = request.form['review']
    inputs = tokenizer(review, return_tensors='pt', truncation=True, padding=True)
    
    with torch.no_grad():
        output = model(inputs['input_ids'])
        prediction = torch.sigmoid(output).item()

    result = "Positive" if prediction >= 0.5 else "Negative"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
