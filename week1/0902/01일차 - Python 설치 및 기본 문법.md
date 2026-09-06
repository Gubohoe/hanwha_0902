# 0902 - 개발환경 및 Python 기본 문법

## 1. 개발환경

### Python

Python은 다양한 분야에서 활용되는 프로그래밍 언어이다.

* 데이터 분석
* 인공지능 및 머신러닝
* 웹 개발
* 자동화
* 백엔드 개발

Python 설치 후 버전을 확인할 수 있다.

```bash
python --version
```

---

### VS Code

VS Code(Visual Studio Code)는 소스 코드를 작성하고 실행할 수 있는 코드 편집기이다.

Python 개발 시 Python Extension을 설치하여 사용할 수 있다.

---

## 2. 가상환경

가상환경은 프로젝트마다 독립적인 Python 실행 환경을 구성하기 위해 사용한다.

### 가상환경 생성

```bash
python -m venv venv
```

### 가상환경 활성화


```bash
venv\Scripts\activate
```

### 가상환경 비활성화

```bash
deactivate
```

### 가상환경을 사용하는 이유

프로젝트마다 사용하는 라이브러리와 버전이 다를 수 있기 때문에 가상환경을 사용하면 프로젝트별 환경을 독립적으로 관리할 수 있다.

* 패키지 버전 충돌 방지
* 프로젝트별 환경 분리
* 필요한 라이브러리만 설치
* 시스템 환경에 영향을 최소화

---

# 3. Python 문법

## 3.1 변수

변수는 데이터를 저장하기 위한 이름이다.

```python
name = "Python"
age = 20
height = 175.5
```

Python에서는 변수 선언 시 자료형을 직접 작성하지 않는다.

```python
x = 10
x = "hello"
```

하나의 변수에 다른 자료형의 값을 다시 저장할 수도 있다.

---

## 3.2 형변환

자료형을 다른 자료형으로 변환하는 것을 형변환이라고 한다.

### 문자열 → 정수

```python
num = int("10")

print(num)
print(type(num))
```

### 정수 → 문자열

```python
num = 10

text = str(num)

print(text)
print(type(text))
```

### 문자열 → 실수

```python
num = float("3.14")

print(num)
```

주요 형변환 함수:

| 함수        | 변환  |
| --------- | --- |
| `int()`   | 정수  |
| `float()` | 실수  |
| `str()`   | 문자열 |
| `bool()`  | 논리형 |

---

## 3.3 리스트

리스트는 여러 개의 데이터를 하나의 자료형으로 관리할 수 있다.

```python
numbers = [1, 2, 3, 4, 5]
```

### 리스트의 길이

```python
print(len(numbers))
```

---

## 3.4 반복문

반복문은 동일하거나 유사한 작업을 반복해서 실행할 때 사용한다.

### for문

```python
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)
```

`range()`를 이용할 수도 있다.

```python
for i in range(5):
    print(i)
```

---

## 3.5 함수

함수는 특정 작업을 수행하는 코드를 하나로 묶어 재사용할 수 있도록 만든 것이다.

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

### 함수의 기본 구조

```python
def 함수이름(매개변수):
    실행할 코드
    return 반환값
```

---

# ⭐ 오늘의 핵심

* Python과 VS Code 개발환경 구성
* Python 가상환경 생성 및 활성화
* 변수와 자료형
* 형변환
* 리스트
* 반복문
* 함수 정의와 호출
