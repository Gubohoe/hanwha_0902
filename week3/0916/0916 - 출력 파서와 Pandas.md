# 0916 - 출력 파서와 Pandas

## 1. 오늘 학습 내용

- 출력 파서(Output Parser)
  - `PydanticOutputParser`
  - `with_structured_output()`
  - `CommaSeparatedListOutputParser`
  - `StructuredOutputParser`
  - `JsonOutputParser`
  - `PandasDataFrameOutputParser`
  - `DateTimeOutputParser`
  - `EnumOutputParser`
- `pandas` 라이브러리

---

# 2. 출력 파서(Output Parser)

## 2.1 출력 파서란?

LLM은 기본적으로 **자유로운 문자열(Text)​**을 반환한다.

예를 들어 사용자에게 다음과 같이 질문했다고 하자.

```text
서울의 대표적인 관광지 3개를 알려줘.
```

LLM은 다음처럼 답할 수 있다.

```text
서울의 대표적인 관광지로는 경복궁, 남산타워, 명동이 있습니다.
```

사람이 읽기에는 문제가 없지만, 프로그램에서 사용하려면 불편하다.

예를 들어 프로그램에서 관광지를 리스트로 사용하고 싶다면 다음과 같은 형태가 더 적합하다.

```python
["경복궁", "남산타워", "명동"]
```

즉,

```text
LLM의 자연어 출력
        ↓
출력 파서(Output Parser)
        ↓
프로그램에서 사용하기 좋은 구조
```

로 변환하는 것이 출력 파서의 역할이다.

---

## 2.2 출력 파서를 사용하는 이유

LLM의 출력은 항상 일정한 형식이라고 보장할 수 없다.

예를 들어 다음과 같은 요청을 했다고 하자.

```text
이름과 나이를 JSON 형식으로 알려줘.
```

LLM이 다음처럼 출력할 수도 있다.

```json
{
  "name": "홍길동",
  "age": 25
}
```

하지만 경우에 따라 설명을 추가할 수도 있다.

```text
물론입니다. 다음은 요청하신 정보입니다.

{
  "name": "홍길동",
  "age": 25
}
```

프로그램에서 바로 사용하기에는 문제가 발생할 수 있다.

출력 파서는 LLM의 결과를 **정해진 형식으로 파싱하고 검증**하는 데 사용한다.

---

# 3. PydanticOutputParser

## 3.1 PydanticOutputParser란?

`PydanticOutputParser`는 LLM의 출력을 **Pydantic 모델 객체**로 변환하는 출력 파서이다.

Pydantic 모델을 사용하기 때문에 원하는 데이터 구조와 타입을 명확하게 정의할 수 있다.

```python
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser


class Person(BaseModel):
    name: str
    age: int


parser = PydanticOutputParser(pydantic_object=Person)
```

LLM에게 전달할 프롬프트에는 parser가 요구하는 출력 형식을 포함시킬 수 있다.

```python
format_instructions = parser.get_format_instructions()
```

예를 들어 프롬프트에서:

```python
prompt = f"""
사람의 이름과 나이를 알려줘.

{format_instructions}
"""
```

와 같이 사용할 수 있다.

---

## 3.2 파싱 결과

LLM이 다음과 같은 JSON 형태를 반환했다고 가정하자.

```json
{
    "name": "홍길동",
    "age": 25
}
```

파서를 거치면:

```python
result = parser.parse(llm_output)
```

결과는 Pydantic 객체가 된다.

```python
print(result.name)
print(result.age)
```

출력:

```text
홍길동
25
```

---

## 3.3 핵심

```text
LLM 문자열
   ↓
PydanticOutputParser
   ↓
Pydantic 객체
```

**장점**

- 데이터 구조를 명확하게 정의할 수 있다.
- 타입 검증이 가능하다.
- Python 코드에서 객체 형태로 편리하게 사용할 수 있다.

---

# 4. with_structured_output()

## 4.1 개념

LangChain에서는 모델에 구조화된 출력을 직접 요청하는 방법으로

```python
with_structured_output()
```

을 사용할 수 있다.

예를 들어 Pydantic 모델을 정의한다.

```python
from pydantic import BaseModel


class Person(BaseModel):
    name: str
    age: int
```

그리고 모델에 연결한다.

```python
structured_llm = llm.with_structured_output(Person)
```

이후 호출하면:

```python
result = structured_llm.invoke("홍길동은 25살이다.")
```

결과를 `Person` 형태로 받을 수 있다.

```python
print(result.name)
print(result.age)
```

---

## 4.2 PydanticOutputParser와 차이

두 방법 모두 구조화된 결과를 얻을 수 있지만 접근 방식에 차이가 있다.

### PydanticOutputParser

```text
LLM
 ↓
텍스트 출력
 ↓
PydanticOutputParser
 ↓
Pydantic 객체
```

즉, **LLM 출력 결과를 파서가 후처리**한다.

### with_structured_output()

```text
LLM
 ↓
구조화된 출력 요청
 ↓
Pydantic 객체
```

모델이 지원하는 구조화 출력 기능을 활용하여 원하는 스키마에 맞춰 결과를 받는다.

따라서 최신 LangChain 기반 애플리케이션에서는 모델이 지원한다면 `with_structured_output()`이 간결한 선택지가 될 수 있다.

---

# 5. CommaSeparatedListOutputParser

## 5.1 개념

`CommaSeparatedListOutputParser`는 LLM의 출력을 **쉼표로 구분된 리스트**로 변환하는 파서이다.

예를 들어 LLM이 다음을 출력한다.

```text
사과, 바나나, 오렌지
```

파서를 사용하면:

```python
["사과", "바나나", "오렌지"]
```

형태로 사용할 수 있다.

---

## 5.2 사용 예시

```python
from langchain_core.output_parsers import CommaSeparatedListOutputParser

parser = CommaSeparatedListOutputParser()

result = parser.parse("사과, 바나나, 오렌지")

print(result)
```

결과:

```python
["사과", "바나나", "오렌지"]
```

---

## 5.3 활용

예를 들어 LLM에게:

```text
Python으로 할 수 있는 작업 5개를 알려줘.
```

라고 요청하고,

```text
웹 개발, 데이터 분석, 인공지능, 자동화, 머신러닝
```

처럼 답변하도록 만든 후 리스트로 변환할 수 있다.

---

# 6. StructuredOutputParser

## 6.1 개념

`StructuredOutputParser`는 LLM의 출력을 **미리 정의한 여러 개의 필드**를 가진 구조로 파싱할 때 사용할 수 있다.

예를 들어 다음과 같은 결과를 받고 싶다고 하자.

```text
answer: 서울
reason: 대한민국의 수도
```

먼저 응답 구조를 정의한다.

```python
from langchain.output_parsers import StructuredOutputParser
from langchain.output_parsers import ResponseSchema


response_schemas = [
    ResponseSchema(
        name="answer",
        description="질문에 대한 답변"
    ),
    ResponseSchema(
        name="reason",
        description="답변에 대한 이유"
    )
]

parser = StructuredOutputParser.from_response_schemas(
    response_schemas
)
```

그리고 형식 지침을 가져올 수 있다.

```python
format_instructions = parser.get_format_instructions()
```

이를 프롬프트에 포함한다.

```python
prompt = f"""
대한민국의 수도는 어디인가?

{format_instructions}
"""
```

---

## 6.2 핵심

```text
ResponseSchema
      ↓
출력 형식 정의
      ↓
StructuredOutputParser
      ↓
구조화된 결과
```

여러 필드를 가진 응답을 일정한 형태로 받고 싶을 때 사용할 수 있다.

---

# 7. JsonOutputParser

## 7.1 개념

`JsonOutputParser`는 LLM의 출력을 **JSON 형태로 파싱**한다.

JSON은 AI 서비스에서 매우 자주 사용되는 데이터 형식이다.

예:

```json
{
    "name": "홍길동",
    "age": 25
}
```

Python에서는 딕셔너리와 비슷하게 사용할 수 있다.

```python
result["name"]
result["age"]
```

---

## 7.2 예시

```python
from langchain_core.output_parsers import JsonOutputParser

parser = JsonOutputParser()

result = parser.parse("""
{
    "name": "홍길동",
    "age": 25
}
""")

print(result)
```

결과:

```python
{
    "name": "홍길동",
    "age": 25
}
```

---

## 7.3 활용

API 서버를 만들 때 특히 유용하다.

예를 들어 LLM이:

```json
{
    "answer": "파이썬은 프로그래밍 언어입니다.",
    "confidence": 0.95
}
```

형태로 응답하면 FastAPI 등의 서버에서 데이터를 처리하기 쉽다.

---

# 8. PandasDataFrameOutputParser

## 8.1 개념

`PandasDataFrameOutputParser`는 LLM의 출력을 **Pandas DataFrame 형태로 처리**할 때 사용하는 파서이다.

데이터 분석이나 표 형태의 결과를 처리할 때 활용할 수 있다.

예를 들어 다음과 같은 데이터를 생각할 수 있다.

```text
이름 | 나이 | 점수
홍길동 | 25 | 90
김철수 | 23 | 85
이영희 | 24 | 95
```

이를 데이터프레임 형태로 처리할 수 있다.

```text
LLM 출력
   ↓
PandasDataFrameOutputParser
   ↓
Pandas DataFrame
```

---

# 9. Pandas 라이브러리

## 9.1 Pandas란?

`pandas`는 Python에서 **데이터를 처리하고 분석하기 위한 라이브러리**이다.

특히 표 형태의 데이터를 다룰 때 많이 사용한다.

```python
import pandas as pd
```

Pandas의 핵심 자료구조는 다음 두 가지이다.

| 자료구조 | 설명 |
|---|---|
| Series | 1차원 데이터 |
| DataFrame | 2차원 표 형태 데이터 |

---

# 10. DataFrame

## 10.1 DataFrame 만들기

```python
import pandas as pd

data = {
    "name": ["홍길동", "김철수", "이영희"],
    "age": [25, 23, 24],
    "score": [90, 85, 95]
}

df = pd.DataFrame(data)

print(df)
```

결과:

```text
   name  age  score
0  홍길동   25     90
1  김철수   23     85
2  이영희   24     95
```

---

# 11. DataFrame 기본 사용법

## 11.1 열 선택

```python
df["name"]
```

여러 열을 선택할 수도 있다.

```python
df[["name", "score"]]
```

---

## 11.2 행 선택

```python
df.iloc[0]
```

첫 번째 행을 가져온다.

```python
df.iloc[0:2]
```

첫 번째부터 두 번째 행까지 가져온다.

---

## 11.3 조건으로 데이터 선택

```python
df[df["age"] >= 24]
```

나이가 24세 이상인 데이터만 선택한다.

---

## 11.4 새로운 열 추가

```python
df["passed"] = df["score"] >= 90
```

결과:

```text
   name  age  score  passed
0  홍길동   25     90    True
1  김철수   23     85   False
2  이영희   24     95    True
```

---

## 11.5 평균 계산

```python
df["score"].mean()
```

점수의 평균을 계산한다.

---

## 11.6 CSV 읽기

Pandas는 CSV 파일을 읽는 데도 자주 사용된다.

```python
df = pd.read_csv("data.csv")
```

CSV 파일을 DataFrame으로 가져온다.

---

## 11.7 CSV 저장

```python
df.to_csv("result.csv", index=False)
```

DataFrame을 CSV 파일로 저장한다.

`index=False`는 DataFrame의 인덱스를 별도 열로 저장하지 않겠다는 의미이다.

---

# 12. DateTimeOutputParser

## 12.1 개념

`DateTimeOutputParser`는 LLM의 출력에서 **날짜와 시간 정보를 파싱**할 때 사용한다.

예를 들어:

```text
2026-09-16 14:30:00
```

과 같은 날짜/시간 데이터를 Python의 `datetime` 객체로 변환하여 사용할 수 있다.

```text
LLM 출력
   ↓
DateTimeOutputParser
   ↓
datetime 객체
```

날짜 계산이나 일정 관리와 같은 애플리케이션에서 활용할 수 있다.

---

# 13. EnumOutputParser

## 13.1 Enum이란?

`Enum`은 **정해진 선택지 중 하나의 값만 사용하도록 제한**할 때 사용하는 기능이다.

예:

```python
from enum import Enum


class Color(Enum):
    RED = "red"
    BLUE = "blue"
    GREEN = "green"
```

이 경우 사용할 수 있는 값은:

```text
red
blue
green
```

으로 제한된다.

---

## 13.2 EnumOutputParser

`EnumOutputParser`는 LLM의 출력이 미리 정의한 Enum 값 중 하나인지 파싱하는 데 사용할 수 있다.

예를 들어 감정을 다음 세 가지로 제한한다고 하자.

```python
from enum import Enum


class Sentiment(Enum):
    POSITIVE = "positive"
    NEGATIVE = "negative"
    NEUTRAL = "neutral"
```

LLM이:

```text
positive
```

를 반환하면 해당 Enum 값으로 처리할 수 있다.

반면:

```text
happy
```

처럼 정의되지 않은 값이 나오면 원하는 형식과 맞지 않기 때문에 문제가 발생할 수 있다.

---

# 14. 출력 파서 종류 비교

| 파서 | 주요 목적 | 결과 |
|---|---|---|
| `PydanticOutputParser` | Pydantic 모델로 변환 | Pydantic 객체 |
| `with_structured_output()` | 구조화된 출력 요청 | 구조화된 객체 |
| `CommaSeparatedListOutputParser` | 쉼표 구분 리스트 | List |
| `StructuredOutputParser` | 여러 필드의 구조화된 출력 | 구조화 데이터 |
| `JsonOutputParser` | JSON 출력 | Dictionary 형태 |
| `PandasDataFrameOutputParser` | 표 형태 데이터 처리 | DataFrame |
| `DateTimeOutputParser` | 날짜/시간 처리 | datetime |
| `EnumOutputParser` | 정해진 선택지 처리 | Enum |

---

# 15. 어떤 파서를 사용해야 할까?

상황에 따라 적절한 파서를 선택한다.

### 리스트가 필요하다

```python
CommaSeparatedListOutputParser
```

```text
사과, 바나나, 오렌지
        ↓
["사과", "바나나", "오렌지"]
```

### JSON이 필요하다

```python
JsonOutputParser
```

```text
LLM
 ↓
JSON
 ↓
Python 데이터
```

### Pydantic 모델이 필요하다

```python
PydanticOutputParser
```

또는 모델이 지원한다면:

```python
with_structured_output()
```

### 표 형태의 데이터가 필요하다

```python
PandasDataFrameOutputParser
```

### 날짜/시간이 필요하다

```python
DateTimeOutputParser
```

### 정해진 선택지 중 하나가 필요하다

```python
EnumOutputParser
```

---

# 16. 출력 파서 전체 흐름

LLM 애플리케이션에서 출력 파서는 다음과 같이 사용할 수 있다.

```text
사용자 입력
    ↓
Prompt
    ↓
LLM
    ↓
LLM의 출력
    ↓
Output Parser
    ↓
정해진 데이터 형식
    ↓
Python 코드에서 활용
```

예를 들어 AI 서비스에서:

```text
사용자 질문
    ↓
LLM
    ↓
JSON 출력
    ↓
JsonOutputParser
    ↓
FastAPI
    ↓
Frontend
```

와 같은 구조를 만들 수 있다.

---

# 17. 출력 파서와 Pydantic의 관계

Pydantic은 **데이터 구조와 타입을 정의하고 검증**하는 역할을 한다.

출력 파서는 **LLM의 결과를 해당 구조로 변환**하는 역할을 한다.

예:

```python
class User(BaseModel):
    name: str
    age: int
```

LLM 출력:

```json
{
    "name": "홍길동",
    "age": 25
}
```

파싱:

```text
LLM 문자열
    ↓
Output Parser
    ↓
User 객체
    ↓
타입과 구조 검증
```

따라서 LLM 애플리케이션에서는

**Prompt → LLM → Parser → 검증된 데이터**

라는 흐름이 중요하다.

---

# 18. 오늘의 학습 흐름

```text
Pydantic
   ↓
데이터 구조와 타입 정의
   ↓
LLM
   ↓
자유로운 텍스트 출력
   ↓
Output Parser
   ↓
정해진 데이터 구조로 변환
   ↓
Python에서 활용
   ↓
Pandas
   ↓
표 형태의 데이터 분석
```

특히 **AI 서비스 백엔드**에서는 LLM이 생성한 결과를 그대로 사용하는 것보다, 필요한 형태로 구조화하고 검증한 뒤 FastAPI나 데이터 처리 코드로 넘기는 과정이 중요하다.