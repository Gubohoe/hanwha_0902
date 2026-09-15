# 0910 - 중첩 Dictionary, 제어문, FastAPI와 Streamlit 통신

## 1. 학습 내용

- 중첩 Dictionary
- Python 제어문
- FastAPI와 Streamlit의 포트 통신
- Streamlit을 활용한 간단한 챗봇 구현

---

# 2. 중첩 Dictionary

## 2.1 중첩 Dictionary란?

Dictionary 안에 또 다른 Dictionary가 들어있는 형태이다.

```python
users = {
    "user1": {
        "name": "Kim",
        "age": 20
    },
    "user2": {
        "name": "Lee",
        "age": 25
    }
}
```

구조를 그림으로 표현하면:

```text
users
 ├── user1
 │    ├── name → Kim
 │    └── age  → 20
 │
 └── user2
      ├── name → Lee
      └── age  → 25
```

---

## 2.2 중첩 Dictionary 데이터 접근

```python
users["user1"]
```

결과:

```python
{
    "name": "Kim",
    "age": 20
}
```

특정 값에 접근하려면:

```python
users["user1"]["name"]
```

결과:

```text
Kim
```

```python
users["user1"]["age"]
```

결과:

```text
20
```

---

## 2.3 데이터 추가 및 수정

값 수정:

```python
users["user1"]["age"] = 21
```

새로운 사용자 추가:

```python
users["user3"] = {
    "name": "Park",
    "age": 30
}
```

---

### 핵심

> 중첩 Dictionary는 계층적인 데이터를 표현할 때 유용하다.

예:

- 사용자 정보
- 상품 정보
- JSON 데이터
- API Response
- 설정 정보

---

# 3. 제어문

제어문은 프로그램의 **실행 흐름을 제어**하기 위해 사용한다.

대표적으로:

```text
조건문 → if / elif / else
반복문 → for / while
```

---

## 3.1 if 조건문

조건에 따라 실행할 코드를 결정한다.

```python
age = 20

if age >= 20:
    print("성인입니다.")
else:
    print("미성년자입니다.")
```

---

## 3.2 elif

여러 조건을 확인할 때 사용한다.

```python
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
```

조건은 위에서부터 순서대로 확인한다.

---

## 3.3 for 반복문

자료의 요소를 하나씩 반복해서 처리할 때 사용한다.

```python
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)
```

실행 결과:

```text
1
2
3
4
5
```

Dictionary에서도 사용할 수 있다.

```python
for key, value in users.items():
    print(key, value)
```

---

## 3.4 while 반복문

조건이 참인 동안 반복한다.

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

---

## 3.5 break와 continue

### break

반복문을 즉시 종료한다.

```python
for i in range(10):
    if i == 5:
        break

    print(i)
```

결과:

```text
0
1
2
3
4
```

### continue

현재 반복을 건너뛰고 다음 반복으로 넘어간다.

```python
for i in range(5):
    if i == 2:
        continue

    print(i)
```

결과:

```text
0
1
3
4
```

---

# 4. FastAPI와 Streamlit

## 4.1 FastAPI와 Streamlit의 역할

FastAPI와 Streamlit은 서로 다른 역할을 담당할 수 있다.

### FastAPI

**백엔드 / API 서버**

```text
데이터 처리
비즈니스 로직
AI 모델
DB
API 제공
```

### Streamlit

**프론트엔드 / 사용자 인터페이스**

```text
화면 구성
사용자 입력
버튼
채팅 UI
API 요청
결과 표시
```

구조:

```text
┌──────────────┐
│   사용자     │
└──────┬───────┘
       ↓
┌──────────────┐
│  Streamlit   │
│   Frontend   │
└──────┬───────┘
       │ HTTP Request
       ↓
┌──────────────┐
│   FastAPI    │
│   Backend    │
└──────┬───────┘
       ↓
  데이터 / AI / DB
```

---

# 5. 포트 통신

## 5.1 포트란?

한 컴퓨터에서 여러 프로그램이 네트워크 통신을 할 수 있도록 구분해주는 번호이다.

예를 들어:

```text
FastAPI   → 8000번 포트
Streamlit → 8501번 포트
```

두 프로그램은 같은 컴퓨터에서 실행되더라도 서로 다른 포트를 사용할 수 있다.

```text
localhost:8000
localhost:8501
```

---

## 5.2 FastAPI 서버 실행

예를 들어 FastAPI를 다음과 같이 실행한다.

```bash
uvicorn main:app --reload --port 8000
```

그러면 FastAPI 서버는:

```text
http://localhost:8000
```

에서 실행된다.

---

## 5.3 Streamlit 서버 실행

```bash
streamlit run app.py
```

일반적으로 Streamlit은:

```text
http://localhost:8501
```

에서 실행된다.

---

## 5.4 Streamlit에서 FastAPI 호출

Streamlit에서 HTTP 요청을 보내 FastAPI의 API를 사용할 수 있다.

예:

```python
import requests

response = requests.get(
    "http://localhost:8000/users"
)

data = response.json()

st.write(data)
```

전체적인 통신 과정:

```text
Streamlit
   │
   │ GET /users
   ↓
FastAPI : 8000
   │
   │ 데이터 처리
   ↓
Response
   │
   ↓
Streamlit : 8501
   │
   ↓
화면에 결과 출력
```

---

# 8. 오늘의 핵심 정리

### 중첩 Dictionary

```python
data["user"]["name"]
```

> Dictionary 안에 Dictionary가 들어있는 구조

### 제어문

```text
if / elif / else → 조건에 따른 실행
for / while       → 반복 실행
break             → 반복 종료
continue          → 현재 반복 건너뛰기
```

### FastAPI + Streamlit

```text
Streamlit
   ↓ HTTP Request
FastAPI
   ↓
데이터 / AI 처리
   ↓
HTTP Response
   ↓
Streamlit
```

### 포트

```text
FastAPI   → :8000
Streamlit → :8501
```

> 서로 다른 포트에서 실행되는 프로그램끼리 HTTP 요청과 응답을 통해 통신할 수 있다.

