# 0908 - 데코레이터, async/await, 프레임워크와 라이브러리, FastAPI, 웹 오류 코드

## 1. 학습 내용

- Python 데코레이터(Decorator)
- `async/await`와 비동기 프로그래밍
- 프레임워크(Framework)와 라이브러리(Library)의 차이
- FastAPI
- 웹 HTTP 오류 코드의 의미

---

## 2. 데코레이터(Decorator)

### 2.1 데코레이터란?

데코레이터는 **함수나 클래스의 코드를 직접 수정하지 않고 기능을 추가하거나 변경하는 방법**이다.

함수를 다른 함수로 감싸서 기존 함수에 새로운 동작을 추가할 수 있다.

```python
def decorator(func):
    def wrapper():
        print("함수 실행 전")
        func()
        print("함수 실행 후")

    return wrapper
```

사용할 때는 `@` 문법을 사용한다.

```python
@decorator
def hello():
    print("Hello!")
```

실행:

```text
함수 실행 전
Hello!
함수 실행 후
```

즉,

```python
@decorator
def hello():
    ...
```

는 다음과 비슷한 의미이다.

```python
hello = decorator(hello)
```

### 2.2 데코레이터를 사용하는 이유

반복적으로 필요한 기능을 여러 함수에 적용할 때 유용하다.

예를 들어:

- 실행 시간 측정
- 로그 기록
- 권한 검사
- 인증 확인
- 예외 처리
- 캐싱

등에 사용할 수 있다.

### 2.3 인자를 받는 함수의 데코레이터

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print("실행 전")
        result = func(*args, **kwargs)
        print("실행 후")
        return result

    return wrapper
```

`*args`, `**kwargs`를 사용하면 다양한 형태의 인자를 받는 함수를 처리할 수 있다.

### 핵심

> 데코레이터 = 기존 코드를 수정하지 않고 함수에 기능을 추가하는 방법

---

## 3. async / await

### 3.1 동기와 비동기

#### 동기(Synchronous)

작업을 순서대로 하나씩 처리한다.

```text
작업 A 시작
    ↓
작업 A 완료
    ↓
작업 B 시작
    ↓
작업 B 완료
```

앞의 작업이 끝날 때까지 다음 작업을 기다린다.

#### 비동기(Asynchronous)

작업이 기다리는 동안 다른 작업을 처리할 수 있다.

```text
작업 A 시작
    ↓
A가 I/O를 기다리는 동안
    ↓
작업 B 처리
    ↓
작업 A 완료
```

특히 다음과 같은 **I/O 작업**에서 효과적이다.

- 네트워크 요청
- 데이터베이스 요청
- 파일 입출력
- API 호출

---

### 3.2 async

`async`를 사용하면 비동기 함수를 정의할 수 있다.

```python
async def hello():
    print("Hello")
```

이런 함수를 **코루틴(coroutine)​**이라고 한다.

---

### 3.3 await

`await`는 비동기 작업의 결과를 기다리는 데 사용한다.

```python
async def hello():
    result = await some_function()
    return result
```

단, `await`는 일반 함수가 아니라 **async 함수 내부에서 사용**해야 한다.

---

### 3.4 예시

```python
import asyncio

async def task():
    print("작업 시작")
    await asyncio.sleep(2)
    print("작업 완료")

asyncio.run(task())
```

`asyncio.sleep(2)`를 기다리는 동안 다른 비동기 작업을 실행할 수 있다.

### 핵심

```text
async → 비동기 함수 정의
await → 비동기 작업을 기다림
```

---

## 4. 프레임워크와 라이브러리의 차이

### 4.1 라이브러리(Library)

개발자가 필요할 때 **직접 호출해서 사용하는 도구**이다.

```text
개발자
  ↓
라이브러리 호출
  ↓
필요한 기능 사용
```

예:

- NumPy
- Pandas
- Matplotlib

개발자가 프로그램의 전체 흐름을 결정한다.

---

### 4.2 프레임워크(Framework)

프로그램의 **전체적인 구조와 실행 흐름을 제공**한다.

```text
프레임워크
    ↓
프로그램의 흐름을 관리
    ↓
개발자가 필요한 부분을 구현
```

예:

- FastAPI
- Django
- Spring

프레임워크가 정해진 구조에 따라 프로그램을 실행하고, 개발자는 그 구조에 맞춰 코드를 작성한다.

### 4.3 가장 중요한 차이

**제어의 주체가 누구인가?**

| 구분 | 라이브러리 | 프레임워크 |
|---|---|---|
| 제어 흐름 | 개발자가 제어 | 프레임워크가 제어 |
| 사용 방식 | 필요한 기능을 호출 | 프레임워크 구조에 맞춰 개발 |
| 예시 | NumPy, Pandas | FastAPI, Django |

이를 **제어의 역전(IoC, Inversion of Control)​**이라고 한다.

> 라이브러리: 내가 라이브러리를 호출한다.  
> 프레임워크: 프레임워크가 내가 작성한 코드를 호출한다.

---

# 5. FastAPI

## 5.1 FastAPI란?

FastAPI는 Python으로 **웹 API를 빠르게 개발할 수 있도록 만들어진 웹 프레임워크**이다.

특징:

- Python 기반
- 빠른 성능
- 비동기 프로그래밍 지원
- 타입 힌트 활용
- 자동 API 문서 생성
- Pydantic을 이용한 데이터 검증

---

## 5.2 기본 FastAPI 코드

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

각 부분의 의미:

```python
app = FastAPI()
```

FastAPI 애플리케이션 객체를 생성한다.

```python
@app.get("/")
```

`GET /` 요청이 들어왔을 때 실행할 함수를 등록한다.

```python
async def root():
```

비동기 방식으로 요청을 처리한다.

```python
return {"message": "Hello World"}
```

클라이언트에게 JSON 형태의 데이터를 반환한다.

---

## 5.3 API와 HTTP 메서드

대표적인 HTTP 메서드:

| 메서드 | 의미 |
|---|---|
| GET | 데이터 조회 |
| POST | 데이터 생성 |
| PUT | 데이터 전체 수정 |
| PATCH | 데이터 일부 수정 |
| DELETE | 데이터 삭제 |

예:

```python
@app.get("/users")
async def get_users():
    ...
```

사용자 정보를 조회하는 API를 만들 수 있다.

```python
@app.post("/users")
async def create_user():
    ...
```

사용자를 생성하는 API를 만들 수 있다.

---

# 6. 웹 오류 코드

HTTP 상태 코드는 서버가 클라이언트의 요청을 어떻게 처리했는지 알려주는 숫자이다.

## 6.1 2xx - 성공

### 200 OK

요청이 정상적으로 처리되었다.

```text
GET /users
→ 200 OK
```

### 201 Created

요청이 정상적으로 처리되어 새로운 리소스가 생성되었다.

주로 `POST` 요청에서 사용한다.

```text
POST /users
→ 201 Created
```

---

# 7. 4xx - 클라이언트 요청 오류

클라이언트의 요청에 문제가 있는 경우이다.

### 400 Bad Request

잘못된 요청이다.

```text
잘못된 데이터 형식
잘못된 요청 파라미터
```

### 401 Unauthorized

인증이 필요한데 인증되지 않은 경우이다.

```text
로그인하지 않은 사용자가
인증이 필요한 API에 접근
```

### 403 Forbidden

인증은 되었지만 **해당 리소스에 접근할 권한이 없는 경우**이다.

```text
로그인 O
권한 X
→ 403
```

### 404 Not Found

요청한 리소스나 URL을 찾을 수 없다.

```text
GET /abc
→ 해당 API가 존재하지 않음
→ 404 Not Found
```

### 422 Unprocessable Entity

요청 형식은 이해했지만 **전달된 데이터가 유효성 검사를 통과하지 못한 경우**이다.

FastAPI에서 Pydantic을 이용한 요청 데이터 검증 과정에서 자주 볼 수 있다.

예:

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
```

다음과 같이 잘못된 데이터를 전달하면:

```json
{
    "name": "Kim",
    "age": "abc"
}
```

`age`가 `int`로 변환될 수 없기 때문에 검증 오류가 발생할 수 있다.

---

# 8. 5xx - 서버 오류

클라이언트의 요청 자체보다는 **서버에서 문제가 발생한 경우**이다.

### 500 Internal Server Error

서버 내부에서 예상하지 못한 오류가 발생했다.

```text
Client
  ↓
Request
  ↓
Server
  ↓
프로그램 오류
  ↓
500
```

개발할 때 가장 먼저 확인해야 하는 오류 중 하나이다.

### 502 Bad Gateway

Gateway 또는 Proxy 서버가 **뒤쪽 서버(Upstream)로부터 잘못된 응답을 받은 경우** 발생한다.

### 503 Service Unavailable

서버가 현재 요청을 처리할 수 없는 상태이다.

예:

- 서버 과부하
- 서버 점검
- 서비스 일시 중단

---

# 9. HTTP 오류 코드 한눈에 정리

| 코드 | 의미 | 분류 |
|---|---|---|
| 200 | 요청 성공 | 2xx |
| 201 | 리소스 생성 성공 | 2xx |
| 400 | 잘못된 요청 | 4xx |
| 401 | 인증 필요 / 인증 실패 | 4xx |
| 403 | 접근 권한 없음 | 4xx |
| 404 | 리소스를 찾을 수 없음 | 4xx |
| 422 | 요청 데이터 검증 실패 | 4xx |
| 500 | 서버 내부 오류 | 5xx |
| 502 | Gateway에서 잘못된 응답 | 5xx |
| 503 | 서비스를 사용할 수 없음 | 5xx |

---

# 10. 오늘의 핵심 정리

### 데코레이터

> 함수의 코드를 직접 수정하지 않고 기능을 추가한다.

```python
@decorator
def function():
    ...
```

### async / await

> 비동기 작업을 처리하기 위한 문법이다.

```python
async def function():
    result = await task()
```

### 라이브러리 vs 프레임워크

> 라이브러리는 내가 호출하고, 프레임워크는 프레임워크가 전체 흐름을 관리한다.

### FastAPI

> Python으로 빠르고 편리하게 API 서버를 개발할 수 있는 웹 프레임워크이다.

### HTTP 상태 코드

```text
2xx → 성공
4xx → 클라이언트 요청 문제
5xx → 서버 문제
```

특히 다음 코드는 반드시 기억한다.

```text
200 → 성공
201 → 생성 성공
400 → 잘못된 요청
401 → 인증 필요
403 → 권한 없음
404 → 찾을 수 없음
422 → 데이터 검증 실패
500 → 서버 내부 오류
502 → Gateway 오류
503 → 서비스 이용 불가
```