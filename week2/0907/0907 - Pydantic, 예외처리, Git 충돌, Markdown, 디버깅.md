# 0905 - Pydantic, 예외처리, Git 충돌, Markdown, 디버깅

## 1. 학습 내용

- Pydantic
- 예외처리
- Git 충돌 연습
- Markdown 파일
- 디버깅

---

# 2. Pydantic

Pydantic은 Python에서 **데이터의 구조와 타입을 검증하고 관리하기 위한 라이브러리**이다.

특히 API 개발에서 입력 데이터의 형식과 타입을 검증할 때 많이 사용된다.

### 기본 사용법

```python
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int
```

객체를 생성하면서 데이터를 전달할 수 있다.

```python
user = User(
    name="Tom",
    age=20
)

print(user)
```

### 데이터 타입 검증

```python
user = User(
    name="Tom",
    age="20"
)

print(user.age)
```

Pydantic은 입력된 데이터의 타입을 확인하고 필요한 경우 적절하게 변환할 수 있다.

잘못된 데이터가 입력되면 validation error가 발생한다.

### Pydantic의 활용

- 입력 데이터 검증
- 데이터 타입 관리
- API 요청 및 응답 데이터 관리
- FastAPI와 함께 사용

---

# 3. 예외처리

프로그램을 실행하는 과정에서 예상하지 못한 오류가 발생할 수 있다.

Python에서는 `try`, `except` 등을 이용하여 예외를 처리할 수 있다.

## 3.1 try / except

```python
try:
    number = int(input("숫자를 입력하세요: "))
    print(number)
except ValueError:
    print("숫자를 입력해야 합니다.")
```

`try` 블록에서 오류가 발생하면 `except` 블록의 코드가 실행된다.

---

## 3.2 else

예외가 발생하지 않았을 때 실행할 코드는 `else`에 작성할 수 있다.

```python
try:
    number = int(input("숫자를 입력하세요: "))
except ValueError:
    print("잘못된 입력입니다.")
else:
    print(f"입력한 숫자: {number}")
```

---

## 3.3 finally

예외 발생 여부와 관계없이 반드시 실행해야 하는 코드는 `finally`에 작성할 수 있다.

```python
try:
    number = int(input("숫자를 입력하세요: "))
except ValueError:
    print("잘못된 입력입니다.")
finally:
    print("프로그램을 종료합니다.")
```

### 예외처리 구조

```text
try
 ↓
코드 실행
 ↓
예외 발생?
 ├─ Yes → except
 └─ No  → else
 ↓
finally
```

---

# 4. Git 충돌

Git을 이용하여 여러 사람이 하나의 프로젝트를 함께 작업하면 동일한 파일의 같은 부분을 수정하는 상황이 발생할 수 있다.

이때 Git에서 **Merge Conflict(병합 충돌)**가 발생할 수 있다.

## 4.1 충돌이 발생하는 상황

예를 들어 같은 파일의 동일한 부분을 서로 다르게 수정한 경우:

```text
<<<<<<< HEAD
현재 브랜치의 코드
=======
다른 브랜치의 코드
>>>>>>> other-branch
```

Git은 어느 코드를 사용할지 자동으로 결정하지 못하기 때문에 개발자가 직접 수정해야 한다.

---

## 4.2 충돌 해결 과정

일반적인 충돌 해결 과정:

```text
1. Git 충돌 발생
       ↓
2. 충돌이 발생한 파일 확인
       ↓
3. 충돌 부분 수정
       ↓
4. 충돌 표시 제거
       ↓
6. git commit
```

---

# 5. Markdown

Markdown은 일반 텍스트에 간단한 문법을 사용하여 문서를 작성할 수 있는 마크업 언어이다.

파일 확장자는 `.md`를 사용한다.

## 5.1 제목

```markdown
# 제목 1
## 제목 2
### 제목 3
```

---

## 5.2 목록

### 순서가 없는 목록

```markdown
- Python
- NumPy
- Git
```

### 순서가 있는 목록

```markdown
1. Python 설치
2. 가상환경 생성
3. 코드 작성
```

---

## 5.3 강조

```markdown
**굵게**

*기울임*

`코드`
```

---

## 5.4 코드 블록

여러 줄의 코드는 백틱 3개를 사용하여 표현한다.

````markdown
```python
print("Hello Python")
```
````

---

## 5.5 표

Markdown에서는 `|` 기호를 이용하여 표를 만들 수 있다.

```markdown
| 이름 | 나이 |
|---|---|
| Tom | 20 |
| Jane | 21 |
```

---

# 6. 디버깅

디버깅(Debugging)은 프로그램에서 발생한 오류를 찾아 원인을 분석하고 수정하는 과정이다.

## 6.1 디버깅이 필요한 이유

프로그램이 예상한 결과와 다르게 동작할 때 코드의 실행 과정을 확인하여 오류의 원인을 찾아야 한다.

---

## 6.2 VS Code 디버깅

VS Code에서는 디버거를 이용하여 코드를 한 줄씩 실행하면서 변수의 상태를 확인할 수 있다.

### 주요 기능

- Breakpoint 설정
- 한 줄씩 실행
- 변수 값 확인
- 함수 내부 실행 과정 확인
- 오류 발생 위치 확인

### Breakpoint

Breakpoint는 프로그램 실행을 특정 코드에서 일시 정지시키는 기능이다.

예를 들어 다음 코드가 있을 때:

```python
def add(a, b):
    result = a + b
    return result


x = 10
y = 20

result = add(x, y)

print(result)
```

`result = a + b` 부분에 Breakpoint를 설정하면 해당 위치에서 프로그램 실행이 멈추고 변수의 값을 확인할 수 있다.

---

# ⭐ 오늘의 핵심

- **Pydantic**은 데이터의 구조와 타입을 검증하는 데 사용한다.
- `try`, `except`, `else`, `finally`를 이용하여 예외를 처리할 수 있다.
- Git에서 같은 부분을 다르게 수정하면 Merge Conflict가 발생할 수 있다.
- Git 충돌은 충돌 부분을 직접 수정한 후 `commit`으로 해결한다.
- Markdown은 간단한 문법으로 문서를 작성할 수 있다.
- 디버깅은 프로그램의 오류 원인을 찾고 수정하는 과정이다.
- VS Code의 Breakpoint를 이용하면 코드 실행 과정을 단계별로 확인할 수 있다.