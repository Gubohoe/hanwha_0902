# 0911 - OpenAI API Key, 환경변수, LangChain, Gemini, requirements

## 1. 학습 내용

- OpenAI API Key
- 환경변수 설정
- API Key 보안 관리
- LangChain
- Gemini API Key
- `requirements.txt`

---

# 2. API Key

## 2.1 API Key란?

API를 사용하기 위해 필요한 **인증용 키**이다.

예를 들어 OpenAI API를 사용하려면 발급받은 API Key를 애플리케이션에 전달해야 한다.

```text
프로그램
   ↓
API Key
   ↓
OpenAI API
   ↓
응답
```

Gemini와 같은 다른 AI API도 API Key를 사용하여 서비스를 인증할 수 있다.

---

## 2.2 API Key를 코드에 직접 작성하면 안 되는 이유

다음과 같이 작성하는 것은 좋지 않다.

```python
api_key = "sk-xxxxxxxxxxxxxxxx"
```

GitHub와 같은 저장소에 코드를 올릴 경우 API Key가 외부에 노출될 수 있다.

API Key가 노출되면 다른 사람이 해당 키를 사용하여 API를 호출할 수 있고, 예상하지 못한 비용이 발생할 수도 있다.

따라서 **API Key는 코드와 분리해서 관리하는 것이 중요하다.**

---

# 3. 환경변수

## 3.1 환경변수란?

환경변수(Environment Variable)는 프로그램 외부에서 설정하고 프로그램이 실행될 때 가져와 사용할 수 있는 값이다.

API Key와 같은 민감한 정보를 코드와 분리해서 관리할 때 활용할 수 있다.

```text
코드
 ↓
환경변수에서 API Key 가져오기
 ↓
API 호출
```

---

## 3.2 Python에서 환경변수 사용

Python에서는 `os` 모듈을 이용해 환경변수를 가져올 수 있다.

```python
import os

api_key = os.getenv("OPENAI_API_KEY")
```

환경변수 이름은 원하는 이름으로 정할 수 있지만 일반적으로 의미가 명확하도록 작성한다.

예:

```text
OPENAI_API_KEY
GEMINI_API_KEY
```

---

# 4. `.env` 파일

개발 환경에서는 `.env` 파일에 환경변수를 저장하고 사용하는 방법도 많이 사용한다.

예:

```env
OPENAI_API_KEY=your_openai_api_key
GEMINI_API_KEY=your_gemini_api_key
```

Python에서는 `python-dotenv`를 이용하여 `.env` 파일을 읽을 수 있다.

```python
from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")
```

---

## 4.1 `.gitignore`

`.env` 파일은 API Key가 들어 있기 때문에 Git에 올라가지 않도록 해야 한다.

`.gitignore`에 다음을 추가한다.

```text
.env
```

구조:

```text
프로젝트
├── .env
├── .gitignore
├── main.py
└── requirements.txt
```

```text
.env
  ↓
Git 추적에서 제외
  ↓
GitHub에 API Key가 올라가지 않음
```

### 핵심

> **API Key는 코드에 직접 작성하지 않고 환경변수 등을 이용하여 관리한다.**

---

# 5. OpenAI API Key

OpenAI API를 사용하기 위해서는 API Key가 필요하다.

환경변수에 API Key를 저장하고 애플리케이션에서 불러와 사용할 수 있다.

```python
import os

api_key = os.getenv("OPENAI_API_KEY")
```

이렇게 하면 소스 코드 자체에는 실제 API Key를 작성하지 않아도 된다.

---

# 6. Gemini API Key

Gemini API를 사용하는 경우에도 API Key가 필요하다.

환경변수를 이용하면 다음과 같이 관리할 수 있다.

```env
GEMINI_API_KEY=your_gemini_api_key
```

Python에서:

```python
import os

gemini_api_key = os.getenv("GEMINI_API_KEY")
```

OpenAI와 Gemini처럼 **서로 다른 외부 AI 서비스를 사용할 때 각각의 API Key를 별도로 관리**할 수 있다.

---

# 7. LangChain

## 7.1 LangChain이란?

LangChain은 **LLM을 활용한 애플리케이션을 개발하기 위한 프레임워크/라이브러리 생태계**이다.

LLM을 단순히 한 번 호출하는 것뿐만 아니라 여러 기능을 연결하여 AI 애플리케이션을 만들 수 있도록 도와준다.

예:

- LLM 호출
- Prompt 관리
- 여러 작업 연결
- 대화형 애플리케이션
- 외부 데이터 연결
- RAG
- Agent

---

## 7.2 LangChain의 기본적인 구조

```text
사용자 입력
    ↓
Prompt
    ↓
LangChain
    ↓
LLM
    ↓
응답
```

조금 더 확장하면:

```text
User
 ↓
Prompt
 ↓
LangChain
 ↓
LLM
 ↓
외부 도구 / 데이터
 ↓
결과
 ↓
User
```

---

# 8. LangChain과 LLM

LangChain을 이용하면 특정 LLM을 직접 사용하는 것보다 **애플리케이션의 여러 구성 요소를 연결하고 관리하기 편리하다.**

예를 들어:

```text
사용자 질문
    ↓
Prompt 생성
    ↓
LLM 호출
    ↓
응답 처리
    ↓
사용자에게 반환
```

이러한 흐름을 코드로 구성할 수 있다.

---

# 9. requirements.txt

## 9.1 requirements.txt란?

Python 프로젝트에서 사용하는 **외부 패키지와 버전 정보를 기록하는 파일**이다.

예:

```text
fastapi
uvicorn
streamlit
pydantic
langchain
```

프로젝트에 필요한 패키지를 한 곳에 정리할 수 있다.

---

## 9.2 requirements.txt를 사용하는 이유

다른 컴퓨터에서 프로젝트를 실행할 때 필요한 패키지를 쉽게 설치할 수 있다.

```bash
pip install -r requirements.txt
```

동작:

```text
requirements.txt
       ↓
필요한 패키지 목록 확인
       ↓
pip install
       ↓
개발 환경 구성
```

---

## 9.3 버전 지정

패키지 버전을 지정할 수도 있다.

```text
fastapi==0.116.1
pydantic==2.x.x
```

버전을 지정하면 다른 환경에서도 동일하거나 호환되는 버전의 패키지를 설치할 수 있어 **환경 재현성**을 높이는 데 도움이 된다.

---
## 9.4 `pip freeze`

`pip freeze`는 현재 가상환경에 **설치되어 있는 Python 패키지와 버전을 출력**하는 명령어이다.

```bash
pip freeze
```

실행하면 다음과 같이 설치된 패키지와 버전을 확인할 수 있다.

```text
fastapi==0.116.1
pydantic==2.11.7
streamlit==1.48.1
uvicorn==0.35.0
```

### requirements.txt로 저장하기

현재 환경의 패키지 목록을 `requirements.txt` 파일로 저장할 수 있다.

```bash
pip freeze > requirements.txt
```

그러면 현재 가상환경에 설치된 패키지와 버전이 `requirements.txt`에 기록된다.

```text
현재 가상환경
     ↓
pip freeze
     ↓
설치된 패키지 + 버전
     ↓
requirements.txt
```

### 다른 환경에서 설치하기

다른 컴퓨터나 새로운 가상환경에서 동일한 패키지를 설치할 때:

```bash
pip install -r requirements.txt
```

를 사용한다.

```text
requirements.txt
       ↓
pip install -r requirements.txt
       ↓
동일한 패키지 환경 구성
```

### `pip freeze`를 사용하는 이유

프로젝트에서 사용한 패키지와 버전을 기록해 두면 다른 개발 환경에서도 **비슷한 Python 환경을 재현**할 수 있다.

특히 팀 프로젝트나 배포 환경에서 유용하다.

### 주의할 점

`pip freeze`는 **현재 가상환경에 설치된 모든 패키지**를 기록한다.

따라서 프로젝트에서 직접 사용하지 않는 패키지까지 `requirements.txt`에 포함될 수 있다.

```text
pip freeze
→ 현재 환경의 모든 설치 패키지

requirements.txt
→ 프로젝트 실행에 필요한 패키지를 관리하는 파일
```

### 핵심 명령어

```bash
# 현재 설치된 패키지 확인
pip freeze

# 현재 환경의 패키지를 requirements.txt에 저장
pip freeze > requirements.txt

# requirements.txt의 패키지 설치
pip install -r requirements.txt
```

> **`pip freeze` = 현재 환경의 패키지 목록을 버전과 함께 확인하는 명령어**

> **`pip freeze > requirements.txt` = 현재 환경을 requirements.txt로 기록**

> **`pip install -r requirements.txt` = 기록된 패키지를 설치하여 환경을 재현**

---


# 10. 전체적인 개발 환경 구조

```text
프로젝트
│
├── main.py
│      │
│      ├── 환경변수에서 API Key 가져오기
│      │
│      └── LangChain / LLM 사용
│
├── .env
│      ├── OPENAI_API_KEY
│      └── GEMINI_API_KEY
│
├── .gitignore
│      └── .env
│
└── requirements.txt
       ├── fastapi
       ├── langchain
       └── 기타 패키지
```

---

# 11. 오늘의 핵심 정리

### API Key

> 외부 API를 사용하기 위한 인증 정보

### 환경변수

> API Key와 같은 설정 정보를 코드와 분리하여 관리

```python
os.getenv("OPENAI_API_KEY")
```

### `.env`

> 로컬 개발 환경에서 환경변수를 저장할 수 있는 파일

### `.gitignore`

> `.env` 같은 민감한 파일이 Git에 올라가지 않도록 관리

### LangChain

> LLM을 활용한 애플리케이션을 구성하고 여러 기능을 연결하는 데 사용하는 프레임워크/생태계

### requirements.txt

> Python 프로젝트에서 필요한 패키지와 버전을 관리하는 파일

```bash
pip install -r requirements.txt
```
