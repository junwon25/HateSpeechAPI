# HateSpeechAPI
>사용자가 문장을 입력하면 욕설인지 아닌지 판별해 결과를 출력해주는 웹 어플리케이션입니다.

## Framework

`Flask`

## Getting Started

### Clone Repository

```
$ git clone https://github.com/junwon25/HateSpeechAPI.git
$ cd HateSpeechAPI
```

## 파일 구조

```
.
├── templates/
│   ├── index.html
│   └── prediction.html
├── train/
│   ├── dataset/
│   │   ├── koco_test_labeling.xlsx
│   │   ├── koco_train_labeled.txt
│   │   └── ssibal_train_labeled.txt
│   └── Final_hatespeech_traincode.ipynb
└── app.py
```
koco_test_labeling.xlsx 는 https://github.com/kocohub/korean-hate-speech.git 의 test.no_label.tsv 를 labeling 한 파일임.
koco_train_labeled.txt 는 https://github.com/kocohub/korean-hate-speech.git 의 labeled/train.tsv 파일을 txt로 옮긴 파일임.
ssibal_train_labeled.txt 는 https://ssibaljinjja.wordpress.com/ 웹페이지를 크롤링해 labeling 한 파일임.
## API 설명
'''
$# API용
$        content = request.get_json(silent=True)
$        hateee = content['chat']
$        hateee = get_prediction(hateee)
$        return hateee
$
$        #Demo 사이트 용
$#         val = request.form #index.html에서 name을 통해 submit한 값들을 val 객체로 전달
$#         print(val)
$#         for key, value in val.items():
$#            hateee = get_prediction(value)
$#         return render_template("prediction.html",result = hateee) #name은 key, name에 저장된 값은 value
'''
### 1) /prediction [POST]
**Request 예시**
```
{
    "chat":"안녕하세요"
}
```

**Response 예시**

```
0
```
