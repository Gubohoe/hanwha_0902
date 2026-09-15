# 0915 - 프롬프트와 PromptTemplate, ChatPromptTemplate, Few-shot

## 1. 학습 내용

- 프롬프트(Prompt)
- `PromptTemplate`
- 파일에서 Template 읽어오기
- `ChatPromptTemplate`
- `MessagesPlaceholder`
- `FewShotPromptTemplate`
- Example Selector
- `FewShotChatMessagePromptTemplate`

---

# 2. 프롬프트(Prompt)

## 2.1 프롬프트란?

프롬프트(Prompt)는 **LLM에게 원하는 작업을 수행하도록 전달하는 입력 또는 지시사항**이다.

예를 들어:

```text
Python에서 리스트와 튜플의 차이를 설명해줘.
```

이것도 하나의 프롬프트이다.

프롬프트를 구체적으로 작성할수록 원하는 형태의 답변을 얻기 쉬워진다.

---

## 2.2 프롬프트의 기본 구성

프롬프트에는 다음과 같은 요소를 포함할 수 있다.

```text
역할(Role)
    ↓
작업(Task)
    ↓
조건/제약사항
    ↓
입력 데이터
    ↓
출력 형식
```

예:

```text
너는 Python 전문 강사야.

다음 질문에 대해 초보자가 이해하기 쉽게 설명해줘.

질문:
{question}

답변은 3개의 항목으로 구성해줘.
```

---

# 3. PromptTemplate

## 3.1 PromptTemplate이란?

`PromptTemplate`은 **반복해서 사용하는 프롬프트의 형식을 미리 정의하고, 필요한 값만 동적으로 넣을 수 있도록 해주는 기능**이다.

예를 들어 매번 다음과 같은 프롬프트를 작성한다고 생각해보자.

```text
Python에 대해 설명해줘.
```

여기서 `Python` 대신 다른 주제를 넣고 싶다면 Template을 사용할 수 있다.

```text
{topic}에 대해 설명해줘.
```

---

## 3.2 기본 사용법

```python
from langchain_core.prompts import PromptTemplate

template = PromptTemplate.from_template(
    "{topic}에 대해 설명해줘."
)

prompt = template.invoke({
    "topic": "Python"
})

print(prompt)
```

결과:

```text
Python에 대해 설명해줘.
```

다른 값을 넣을 수도 있다.

```python
prompt = template.invoke({
    "topic": "FastAPI"
})
```

결과:

```text
FastAPI에 대해 설명해줘.
```

---

## 3.3 Template을 사용하는 이유

프롬프트의 구조와 입력 데이터를 분리할 수 있다.

```text
PromptTemplate
      │
      ├── 고정된 프롬프트 구조
      │
      └── 동적으로 변경되는 변수
```

따라서 같은 형식의 프롬프트를 반복해서 사용할 때 편리하다.

---

# 4. 파일로부터 Template 읽어오기

프롬프트를 Python 코드에 직접 작성하지 않고 **별도의 파일로 관리**할 수도 있다.

예를 들어:

```text
prompts/
└── translate.txt
```

`translate.txt`:

```text
다음 문장을 {language}로 번역해줘.

문장:
{text}
```

Python에서 파일을 읽어서 Template으로 사용할 수 있다.

```python
from langchain_core.prompts import PromptTemplate

with open("prompts/translate.txt", "r", encoding="utf-8") as f:
    template = f.read()

prompt = PromptTemplate.from_template(template)

result = prompt.invoke({
    "language": "영어",
    "text": "안녕하세요."
})

print(result)
```

---

## 4.1 프롬프트를 파일로 관리하는 이유

프롬프트가 복잡해질수록 Python 코드와 분리하는 것이 관리하기 편하다.

```text
Python 코드
    ↓
프롬프트 파일 읽기
    ↓
PromptTemplate
    ↓
변수 입력
    ↓
최종 Prompt
```

장점:

- 프롬프트 수정이 쉬움
- 코드와 프롬프트를 분리할 수 있음
- 긴 프롬프트 관리에 유리
- 여러 프롬프트를 파일별로 관리 가능

---

# 5. ChatPromptTemplate

## 5.1 ChatPromptTemplate이란?

`ChatPromptTemplate`은 **Chat 모델에 전달할 메시지 형태의 프롬프트를 구성**할 때 사용하는 Template이다.

일반적인 Prompt가 하나의 문자열이라면 ChatPromptTemplate은 여러 메시지를 역할별로 구성할 수 있다.

대표적인 역할:

```text
system
human
ai
```

---

## 5.2 기본 사용법

```python
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "너는 친절한 Python 강사야."),
    ("human", "{question}")
])

result = prompt.invoke({
    "question": "리스트와 튜플의 차이를 알려줘."
})

print(result)
```

구조:

```text
System
→ 너는 친절한 Python 강사야.

Human
→ 리스트와 튜플의 차이를 알려줘.
```

---

## 5.3 메시지 역할

### System

LLM의 **역할이나 행동 방식**을 지정한다.

```text
너는 Python 전문 강사야.
```

### Human

사용자가 전달하는 질문이나 요청이다.

```text
FastAPI가 무엇인지 설명해줘.
```

### AI

이전 대화에서 **AI가 답변했던 메시지**를 표현할 수 있다.

---

# 6. MessagesPlaceholder

## 6.1 MessagesPlaceholder란?

`MessagesPlaceholder`는 **여러 개의 메시지를 하나의 변수 위치에 동적으로 삽입**하기 위해 사용한다.

특히 **대화 기록(Chat History)**을 프롬프트에 넣을 때 유용하다.

```text
System
  ↓
MessagesPlaceholder
  ↓
Human
```

---

## 6.2 기본 사용법

```python
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "너는 친절한 AI야."),
    MessagesPlaceholder("history"),
    ("human", "{question}")
])
```

대화 기록을 전달:

```python
from langchain_core.messages import HumanMessage, AIMessage

history = [
    HumanMessage(content="내 이름은 철수야."),
    AIMessage(content="안녕하세요 철수님!")
]

result = prompt.invoke({
    "history": history,
    "question": "내 이름이 뭐라고?"
})
```

전체 구조:

```text
System
→ 너는 친절한 AI야.

History
→ Human: 내 이름은 철수야.
→ AI: 안녕하세요 철수님!

Human
→ 내 이름이 뭐라고?
```

### 핵심

> `MessagesPlaceholder` = 여러 메시지를 원하는 위치에 동적으로 넣기

특히 **챗봇의 대화 기록을 관리할 때 중요**하다.

---

# 7. Few-shot Prompt

## 7.1 Few-shot이란?

Few-shot Prompting은 LLM에게 **몇 개의 예시(Example)를 먼저 보여주고 원하는 작업을 수행하도록 하는 방법**이다.

예:

```text
입력: 나는 행복하다.
출력: 긍정

입력: 나는 오늘 너무 슬프다.
출력: 부정

입력: 오늘 기분이 좋다.
출력:
```

LLM은 앞의 예시를 참고하여:

```text
긍정
```

과 같은 답변을 생성할 수 있다.

---

## 7.2 Zero-shot과 Few-shot

### Zero-shot

예시 없이 바로 요청한다.

```text
다음 문장의 감정을 분류해줘.

"오늘 기분이 좋다."
```

### Few-shot

몇 개의 예시를 함께 제공한다.

```text
문장: 나는 행복하다.
감정: 긍정

문장: 나는 너무 슬프다.
감정: 부정

문장: 오늘 기분이 좋다.
감정:
```

즉:

```text
Zero-shot
→ 예시 없음

Few-shot
→ 예시 제공
```

---

# 8. FewShotPromptTemplate

## 8.1 FewShotPromptTemplate이란?

`FewShotPromptTemplate`은 **여러 개의 예시를 프롬프트에 자동으로 구성하여 넣어주는 Template**이다.

기본 구조:

```text
Examples
   ↓
Example Prompt
   ↓
FewShotPromptTemplate
   ↓
최종 Prompt
```

---

## 8.2 예시

먼저 예시를 정의한다.

```python
examples = [
    {
        "input": "나는 행복하다.",
        "output": "긍정"
    },
    {
        "input": "나는 슬프다.",
        "output": "부정"
    }
]
```

예시 하나의 형식을 정의한다.

```python
from langchain_core.prompts import PromptTemplate

example_prompt = PromptTemplate.from_template(
    "입력: {input}\n출력: {output}"
)
```

Few-shot Template을 만든다.

```python
from langchain_core.prompts import FewShotPromptTemplate

few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="다음 예시를 참고해서 감정을 분류해줘.",
    suffix="입력: {input}\n출력:",
    input_variables=["input"]
)
```

실행:

```python
result = few_shot_prompt.invoke({
    "input": "오늘 정말 기분이 좋아."
})
```

최종적으로 다음과 같은 형태의 프롬프트가 만들어진다.

```text
다음 예시를 참고해서 감정을 분류해줘.

입력: 나는 행복하다.
출력: 긍정

입력: 나는 슬프다.
출력: 부정

입력: 오늘 정말 기분이 좋아.
출력:
```

---

# 9. Example Selector

## 9.1 Example Selector란?

Few-shot에서는 예시를 많이 넣으면 **프롬프트가 길어지고 토큰 사용량이 증가**할 수 있다.

Example Selector를 사용하면 여러 예시 중에서 **현재 입력과 관련성이 높은 예시를 선택**할 수 있다.

```text
전체 Example
    │
    ↓
Example Selector
    │
    ├── 관련도 높은 예시
    ├── 관련도 높은 예시
    └── 관련도 낮은 예시는 제외
              ↓
        Few-shot Prompt
```

---

## 9.2 사용하는 이유

예시가 100개 있다고 가정한다.

```text
Example 1
Example 2
Example 3
...
Example 100
```

사용자의 질문과 관련된 예시가 3개뿐이라면 100개를 모두 넣을 필요가 없다.

```text
100개 Example
      ↓
Example Selector
      ↓
관련된 3개 선택
      ↓
LLM
```

이를 통해:

- Prompt 길이 감소
- Token 사용량 감소
- 불필요한 정보 감소
- 입력과 관련된 예시 제공

등의 효과를 얻을 수 있다.

---

# 10. FewShotChatMessagePromptTemplate

## 10.1 FewShotChatMessagePromptTemplate이란?

`FewShotChatMessagePromptTemplate`은 **Chat 모델에서 Few-shot 예시를 메시지 형태로 구성**하기 위한 Template이다.

일반적인 `FewShotPromptTemplate`이 문자열 중심이라면, `FewShotChatMessagePromptTemplate`은 Chat 모델의 메시지 구조에 맞춰 예시를 구성한다.

---

## 10.2 구조

```text
System
  ↓
Few-shot Examples
  ├── Human Message
  └── AI Message
  ↓
Human
  ↓
실제 질문
```

예:

```text
System:
너는 감정 분류 AI야.

Human:
나는 행복하다.

AI:
긍정

Human:
나는 슬프다.

AI:
부정

Human:
오늘 기분이 좋아.

AI:
```

앞의 `Human → AI` 예시를 보고 마지막 질문에 답하도록 한다.

---

## 10.3 예시 코드

```python
from langchain_core.prompts import (
    ChatPromptTemplate,
    FewShotChatMessagePromptTemplate
)

examples = [
    {
        "input": "나는 행복하다.",
        "output": "긍정"
    },
    {
        "input": "나는 슬프다.",
        "output": "부정"
    }
]

example_prompt = ChatPromptTemplate.from_messages([
    ("human", "{input}"),
    ("ai", "{output}")
])

few_shot_prompt = FewShotChatMessagePromptTemplate(
    examples=examples,
    example_prompt=example_prompt
)

final_prompt = ChatPromptTemplate.from_messages([
    ("system", "너는 감정 분류 AI야."),
    few_shot_prompt,
    ("human", "{input}")
])

result = final_prompt.invoke({
    "input": "오늘 정말 기분이 좋아."
})
```

구조를 보면:

```text
ChatPromptTemplate
        │
        ├── System
        │
        ├── FewShotChatMessagePromptTemplate
        │       ├── Human → Example
        │       └── AI    → Example Answer
        │
        └── Human → 실제 입력
```

---

# 11. Prompt 관련 기능 비교

| 기능 | 역할 |
|---|---|
| `PromptTemplate` | 일반적인 프롬프트 템플릿 |
| 파일 Template | 프롬프트를 파일로 분리하여 관리 |
| `ChatPromptTemplate` | Chat 메시지 기반 프롬프트 구성 |
| `MessagesPlaceholder` | 여러 메시지를 동적으로 삽입 |
| `FewShotPromptTemplate` | 예시를 포함한 프롬프트 생성 |
| Example Selector | 관련성 높은 예시를 선택 |
| `FewShotChatMessagePromptTemplate` | Chat 메시지 형태의 Few-shot 구성 |

---

# 12. 오늘의 핵심 정리

### PromptTemplate

> 프롬프트의 틀을 만들고 변수에 따라 내용을 동적으로 변경

```python
PromptTemplate.from_template(
    "{topic}을 설명해줘."
)
```

### ChatPromptTemplate

> System, Human, AI 등의 메시지 역할을 이용하여 Chat 프롬프트 구성

```python
ChatPromptTemplate.from_messages([
    ("system", "..."),
    ("human", "{question}")
])
```

### MessagesPlaceholder

> 대화 기록처럼 여러 메시지를 동적으로 삽입

```python
MessagesPlaceholder("history")
```

### FewShotPromptTemplate

> 여러 예시를 프롬프트에 포함하여 LLM에게 패턴을 보여줌

```text
Example → Example → 실제 입력
```

### Example Selector

> 많은 예시 중 현재 입력과 관련성이 높은 예시를 선택

```text
전체 예시
   ↓
Example Selector
   ↓
관련 예시
   ↓
LLM
```

### FewShotChatMessagePromptTemplate

> Chat 모델에서 Human → AI 형태의 Few-shot 예시를 메시지로 구성

