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
## API 설명

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
