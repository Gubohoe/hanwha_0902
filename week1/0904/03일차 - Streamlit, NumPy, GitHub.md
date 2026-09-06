# 0904 - Python 문법, NumPy, Git, GitHub

## 1. Python 문법

### 1.1 f-string

f-string은 문자열 안에 변수나 표현식의 값을 쉽게 삽입할 수 있는 문자열 formatting 방법이다.

문자열 앞에 `f`를 붙이고 `{}` 안에 변수를 작성한다.

```python
name = "Python"
age = 20

print(f"이름: {name}, 나이: {age}")
```

표현식을 넣을 수도 있다.

```python
a = 10
b = 20

print(f"{a} + {b} = {a + b}")
```

---

## 1.2 Class / 상속

상속은 기존 클래스의 속성과 메서드를 새로운 클래스가 물려받는 기능이다.

```python
class Animal:
    def speak(self):
        print("소리를 냅니다.")


class Dog(Animal):
    def bark(self):
        print("멍멍!")
```

`Dog` 클래스는 `Animal` 클래스를 상속받았기 때문에 `Animal`의 메서드를 사용할 수 있다.

```python
dog = Dog()

dog.speak()
dog.bark()
```

### 상속의 장점

* 기존 코드 재사용
* 중복 코드 감소
* 클래스 간 관계 표현
* 기능 확장에 유리

---

# 2. 인덱싱

인덱싱은 문자열이나 리스트와 같은 자료에서 특정 위치의 데이터를 가져오는 것이다.

Python의 인덱스는 **0부터 시작**한다.

### 리스트 인덱싱

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[2])
```

결과:

```text
10
30
```

### 음수 인덱스

음수 인덱스를 사용하면 뒤에서부터 접근할 수 있다.

```python
print(numbers[-1])
print(numbers[-2])
```

결과:

```text
50
40
```

---

# 3. 슬라이싱

슬라이싱은 문자열이나 리스트에서 원하는 범위의 데이터를 추출하는 방법이다.

기본 형식:

```python
자료[start:end]
```

`end`에 해당하는 인덱스는 포함되지 않는다.

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

결과:

```text
[20, 30, 40]
```

### 시작 또는 끝 생략

```python
print(numbers[:3])
print(numbers[2:])
```

### 간격 지정

```python
print(numbers[::2])
```

---

# 4. NumPy

NumPy는 Python에서 수치 계산과 배열 연산을 효율적으로 처리하기 위한 라이브러리이다.

### NumPy 불러오기

```python
import numpy as np
```

---

## 4.1 Array

NumPy의 핵심 자료구조는 `array`이다.

### 배열 생성

```python
arr = np.array([1, 2, 3, 4, 5])

print(arr)
```

### 2차원 배열

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr)
```

### 배열의 정보 확인

```python
print(arr.shape)
print(arr.ndim)
print(arr.size)
print(arr.dtype)
```

| 속성      | 설명          |
| ------- | ----------- |
| `shape` | 배열의 각 차원 크기 |
| `ndim`  | 배열의 차원 수    |
| `size`  | 전체 원소의 개수   |
| `dtype` | 배열 원소의 자료형  |

---


# 5. Git

Git은 소스 코드의 변경 이력을 관리하는 **분산 버전 관리 시스템**이다.

---

# 6. GitHub

GitHub는 Git 저장소를 인터넷에서 관리하고 공유할 수 있는 플랫폼이다.

Git을 이용해 관리하는 프로젝트를 GitHub에 업로드하여 다른 사람과 공유하거나 협업할 수 있다.

---

# 7. GitHub Desktop

GitHub Desktop은 Git과 GitHub의 기능을 GUI 환경에서 사용할 수 있도록 제공하는 프로그램이다.

터미널에서 Git 명령어를 직접 입력하지 않고도 Git 저장소를 관리할 수 있다.

### 주요 기능

* Repository 관리
* 변경사항 확인
* Commit
* Push
* Pull
* Branch 관리
* GitHub Repository 연동

---

# ⭐ 오늘의 핵심

* f-string을 이용한 문자열 formatting
* Class의 상속 개념
* 인덱싱과 슬라이싱
* NumPy `array`
* NumPy 배열의 기본 속성
* Git을 이용한 버전 관리
* GitHub를 이용한 원격 저장소 관리
* GitHub Desktop을 이용한 GUI 기반 Git 관리
