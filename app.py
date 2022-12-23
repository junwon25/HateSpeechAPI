from flask import Flask
import pandas as pd
import torch
from torch.nn import functional as F
from torch.utils.data import DataLoader, Dataset
from transformers import AutoTokenizer, ElectraForSequenceClassification, AdamW
from flask import Flask,render_template
from flask import jsonify



from flask import Flask, render_template, request
app = Flask(__name__)


#get model
#model detail : 10539, epoch = 3
hateModel = ElectraForSequenceClassification.from_pretrained("KoElectra_base3")
hateModel.load_state_dict(torch.load("HateModel.pt", map_location=torch.device('cpu')))
hateModel_tokenizer = AutoTokenizer.from_pretrained("KoElectra_base3")

class HateDataset(Dataset):

    def __init__(self, csv_file):
        self.dataset = pd.read_csv(csv_file, sep='\t').dropna(axis=0) 
        self.tokenizer = hateModel_tokenizer
  
    def __len__(self):
        return len(self.dataset)
    def __getitem__(self, idx):
        row = self.dataset.iloc[idx, [0,3]].values
        text = row[0]
        if(row[1] == "none"):
            y = 0
        else:
            y = 1
        inputs = self.tokenizer(
            text, 
            return_tensors='pt',
            truncation=True,
            max_length=256,
            pad_to_max_length=True,
            add_special_tokens=True
        )
        input_ids = inputs['input_ids'][0]
        attention_mask = inputs['attention_mask'][0]
        return input_ids, attention_mask, y

def get_prediction(sentence):
  f = open("userInput.txt", 'w')
  f.writelines("comments	contain_gender_bias	bias	hate\n")
  f.writelines(sentence+"	False	none	none")
  f.close()
  input_data = HateDataset("userInput.txt")
  input_loader = DataLoader(input_data, batch_size=1, shuffle=True)

  hateModel.eval()

  #test_correct = 0
  #test_total = 0

  for input_ids_batch, attention_masks_batch, y_batch in input_loader:
    #y_batch = y_batch.to(device)
    y_pred = hateModel(input_ids_batch, attention_mask=attention_masks_batch)[0]
    _, predicted = torch.max(y_pred, 1)
    #test_correct += (predicted == y_batch).sum()
    #test_total += len(y_batch)

    if(predicted.item() == 0):
        return "0"

    else:
        return "1"

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/prediction',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        content = request.get_json(silent=True)
        hateee = content['chat']
        hateee = get_prediction(hateee)
        #val = request.form #index.html에서 name을 통해 submit한 값들을 val 객체로 전달
        #print("웅진파이팅\n")
        #print(val)
        #for key, value in val.items():
        #    hateee = get_prediction(value)
        return hateee
        #return render_template("prediction.html",result = hateee) #name은 key, name에 저장된 값은 value

#FLASK_ENV=development FLASK_APP=app.py flask run
if __name__ =="__main__":
    app.run(host='0.0.0.0', port = 8000)
