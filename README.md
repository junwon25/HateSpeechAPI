# 프로젝트 소개
2022 SKKU 산학협력 프로젝트 - 웅진씽크빅 기업과 함께한 산학협력 프로젝트

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

## 모델 학습
현재 사용된 모델은 koco_train_labeled.txt, ssibal_train_labeled.txt 두 가지를 합친 train dataset을 사용함.
Final_hatespeech_traincode.ipynb 파일은 훈련하는 파트와 검증하는 파트 총 2가지 섹션으로 구성되어있음
txt를 tsv로 변환하는코드, 데이터셋을 구축하는코드, 훈련을 시작하는 코드는 모두 Final_hatespeech_traincode.ipynb에 주석으로 정의되어있으며, Jupyter Notebook이나 Google Colab을 사용해 각 cell을 순서대로 run 하면서 학습을 진행하면 됨.

모델 확인 : https://drive.google.com/file/d/13dx6djTNcncjLuZx1d56WAPD4c6Kgd-Q/view?usp=sharing\

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
![image](https://user-images.githubusercontent.com/96272913/209530793-01c95f3b-0e87-4c12-8b1f-38cb3790648c.png)

- 월드에 있는 대화 그룹에 들어가면 다른 친구들과 자유롭게 대화할 수 있음.
- 대화 내용중에 욕설이 감지되면 왼쪽 상단의 Hate 게이지 바가 올라감.
- Hate 게이지 바가 올라 일정 비율(현재는 40%)이상이 되면 대화 그룹에 우당당탕한 이미지를 띈 막이 형성됨.
- 생성된 막은 그룹에서 욕설이 많이 발생하고 있으니 위험하다는 것을 외부에 알려줌.
