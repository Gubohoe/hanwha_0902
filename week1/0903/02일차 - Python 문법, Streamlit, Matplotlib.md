# 0903 - Python 문법, Colab, Matplotlib, Streamlit

## 1. Python 문법

### 1.1 global

`global` 키워드는 함수 내부에서 전역 변수를 수정할 때 사용한다.

```python
count = 0

def increase():
    global count
    count += 1

increase()

print(count)
```

함수 내부에서 변수를 새로 생성하면 기본적으로 지역 변수로 취급된다.

---

## 1.2 문자열

문자열은 문자들의 집합으로, 작은따옴표 또는 큰따옴표를 사용하여 표현한다.

```python
text1 = "Hello"
text2 = 'Python'
```

### 문자열 연결

```python
first = "Hello"
second = "Python"

result = first + " " + second

print(result)
```

### 문자열 길이

```python
text = "Python"

print(len(text))
```

### 문자열 메서드

```python
text = "Hello Python"

print(text.upper())
print(text.lower())
print(text.replace("Python", "World"))
```

---

# 2. Class / 객체

## 2.1 클래스

클래스는 객체를 생성하기 위한 설계도이다.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"저는 {self.name}이고 {self.age}살입니다.")
```

## 2.2 객체

클래스를 이용하여 실제 객체를 생성할 수 있다.

```python
person = Person("Tom", 20)

person.introduce()
```

### 주요 개념

* **Class**: 객체를 만들기 위한 설계도
* **Object**: 클래스를 이용하여 생성한 실제 데이터
* **Method**: 객체가 수행할 수 있는 기능

---

# 3. Google Colab

Google Colab은 웹 브라우저에서 Python 코드를 작성하고 실행할 수 있는 환경이다.

### 특징

* 별도의 개발환경 설치 없이 사용 가능
* 웹 브라우저에서 Python 실행
* Jupyter Notebook 기반
* 코드와 실행 결과를 하나의 문서에서 관리
* 데이터 분석 및 머신러닝 실습에 활용

### 기본 Python 코드

```python
print("Hello Colab")
```

---

# 4. Matplotlib

Matplotlib은 Python에서 데이터를 시각화하기 위한 라이브러리이다.

### 기본 사용

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Example")

plt.show()
```

### 주요 그래프

| 함수          | 그래프    |
| ----------- | ------ |
| `plot()`    | 선 그래프  |
| `bar()`     | 막대 그래프 |
| `scatter()` | 산점도    |
| `hist()`    | 히스토그램  |
| `pie()`     | 원 그래프  |

---

# 5. Streamlit

Streamlit은 Python을 이용하여 데이터 애플리케이션이나 웹 페이지를 쉽게 만들 수 있도록 도와주는 프레임워크이다.

### 설치

```bash
pip install streamlit
```

### 실행

```bash
streamlit run app.py
```

### 기본 사용

```python
import streamlit as st

st.title("My App")

st.write("Hello Streamlit!")
```

### 사용자 입력

```python
name = st.text_input("이름을 입력하세요.")

if name:
    st.write(f"안녕하세요, {name}님!")
```

### 주요 기능

```python
st.title()
st.header()
st.subheader()
st.write()

st.button()
st.text_input()
st.number_input()
st.selectbox()
st.checkbox()
```

---

# ⭐ 오늘의 핵심

* `global`을 이용한 전역 변수 접근
* Python 문자열 처리
* Class와 Object의 개념
* Google Colab 사용법
* Matplotlib을 이용한 데이터 시각화
* Streamlit을 이용한 웹 애플리케이션 제작
