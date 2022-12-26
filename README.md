# HateSpeechAPI
>사용자가 문장을 입력하면 욕설인지 아닌지 판별해 결과를 출력해주는 웹 어플리케이션입니다.
>ELECTRA를 사용하여 욕설 판별을 진행합니다.
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
모든 api는 app.py에 정의되어 있음 

- koco_test_labeling.xlsx 는 https://github.com/kocohub/korean-hate-speech.git 의 test.no_label.tsv 를 labeling 한 파일임.

- koco_train_labeled.txt 는 https://github.com/kocohub/korean-hate-speech.git 의 labeled/train.tsv 파일을 txt로 옮긴 파일임.

- ssibal_train_labeled.txt 는 https://ssibaljinjja.wordpress.com/ 웹페이지를 크롤링해 labeling 한 파일임.

- tokenizer와 model은 monologg님의 pretrained KoELECTRA model을 사용해 Fine tuning 후 사용 (https://github.com/monologg/KoELECTRA)

## API 설명

사용자가 입력한 문장이 욕설로 판별되면 1, 그렇지 않은 경우에는 0이 반환됩니다.

<API 용>
### 1) /prediction [POST]
**Request 예시1**
```
{
    "chat":"안녕하세요"
}
```

**Response 예시2**

```
0
```

**Request 예시1**
```
{
    "chat":"개새끼야"
}
```

**Response 예시2**

```
1
```

<웹 데모용>
### 1) /prediction [POST] 
**입력 예시**

![image](https://user-images.githubusercontent.com/96272913/209528902-ef0a6d0c-7d7a-47cd-84f3-64190ff55c93.png)

**출력 예시**

![image](https://user-images.githubusercontent.com/96272913/209528952-c1ff13f9-9252-4924-9428-591854d77b56.png)

## 활용예시
