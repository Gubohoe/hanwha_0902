# 0914 - LangChain Invoke, Logprob, Stream, LangSmith, 멀티모달

## 1. 학습 내용

- LangChain
  - `invoke`
  - `logprob`
  - `stream`
- LangSmith
- 멀티모달(Multimodal)

---

# 2. LangChain

LangChain은 LLM을 활용한 애플리케이션을 개발할 때 **프롬프트, 모델, 출력 처리 등의 구성 요소를 연결하고 관리**할 수 있도록 도와주는 프레임워크이다.

기본적인 흐름은 다음과 같다.

```text
사용자 입력
    ↓
Prompt
    ↓
LLM
    ↓
LLM Response
```

LangChain에서는 이러한 구성 요소를 연결하여 하나의 실행 흐름으로 만들 수 있다.

---

# 3. `invoke`

## 3.1 `invoke`란?

`invoke()`는 LangChain의 Runnable 객체를 **실행하고 결과를 반환**할 때 사용하는 메서드이다.

```python
response = chain.invoke("안녕하세요")
```

실행 흐름:

```text
입력
 ↓
invoke()
 ↓
Chain 실행
 ↓
결과 반환
```

예를 들어 LLM을 직접 호출하는 경우:

```python
response = model.invoke("Python이 무엇인가요?")
```

결과를 변수에 저장하여 사용할 수 있다.

```python
print(response)
```

---

## 3.2 `invoke`의 특징

`invoke()`는 **하나의 입력을 전달하고 하나의 결과를 반환받는 기본적인 실행 방식**이라고 이해하면 된다.

```python
result = chain.invoke(input)
```

### 핵심

> `invoke()` = Chain 또는 LLM을 실행하고 결과를 한 번에 받는다.

---

# 4. `stream`

## 4.1 Stream이란?

일반적인 LLM 응답은 모든 답변이 생성된 후 한 번에 전달받을 수 있다.

```text
사용자 질문
    ↓
LLM
    ↓
전체 답변 생성
    ↓
한 번에 출력
```

하지만 `stream()`을 사용하면 LLM이 생성하는 결과를 **조금씩 나누어 실시간으로 전달**받을 수 있다.

```text
사용자 질문
    ↓
LLM
    ↓
"안"
    ↓
"녕"
    ↓
"하"
    ↓
"세"
    ↓
"요"
```

실제 서비스에서는 ChatGPT와 같은 **실시간 답변 출력 UI**를 구현할 때 유용하다.

---

## 4.2 `stream()` 사용

```python
for chunk in model.stream("Python이 무엇인가요?"):
    print(chunk, end="")
```

`stream()`은 결과를 여러 개의 chunk로 나누어 전달한다.

```text
model.stream()
     ↓
chunk 1
chunk 2
chunk 3
chunk 4
     ↓
순차적으로 출력
```

### `invoke`와 `stream` 비교

| 구분 | `invoke()` | `stream()` |
|---|---|---|
| 결과 | 한 번에 반환 | 여러 chunk로 반환 |
| 출력 방식 | 전체 응답 후 출력 | 생성되는 대로 출력 |
| 활용 | 일반적인 요청 | 실시간 응답 |
| 구현 | 간단 | 스트리밍 처리 필요 |

### 핵심

> `invoke()` = 결과를 한 번에 받기  
> `stream()` = 결과를 생성되는 대로 받기

---

# 5. Logprob

## 5.1 Logprob란?

LLM이 다음 토큰을 생성할 때 **각 토큰이 선택될 가능성을 나타내는 값**이다.

LLM은 다음에 어떤 토큰이 나올지 확률적으로 선택한다.

예를 들어:

```text
오늘 날씨가 ___
```

다음 단어에 대해:

```text
좋다  → 높은 확률
춥다  → 낮은 확률
맛있다 → 매우 낮은 확률
```

와 같이 여러 후보에 대한 확률을 계산할 수 있다.

Logprob은 이러한 확률을 **로그 확률(log probability)**로 표현한 값이다.

---

## 5.2 Logprob의 특징

일반적으로 확률은:

```text
0 ~ 1
```

범위를 사용하지만 log를 취하면 값이 음수가 될 수 있다.

```text
확률이 높음
→ logprob가 0에 가까움

확률이 낮음
→ logprob가 더 작은 음수
```

예:

```text
Token     Probability    Logprob
--------------------------------
"좋다"       0.8           -0.22
"춥다"       0.15          -1.90
"맛있다"     0.05          -3.00
```

※ 실제 값은 모델과 설정에 따라 달라진다.

---

## 5.3 Logprob의 활용

Logprob은 모델의 출력에 대한 **확신 정도를 분석**하거나 모델의 토큰 선택을 분석하는 데 활용할 수 있다.

예:

- 모델 출력의 확률 분석
- 토큰별 confidence 분석
- 여러 후보의 선택 확률 비교
- 모델 출력 분석 및 디버깅

단, **logprob가 높다고 해서 모델의 답변이 사실이라는 의미는 아니다.**

> Logprob은 모델이 해당 토큰을 선택할 가능성에 대한 정보이지, 답변의 사실 여부를 직접 보장하는 값은 아니다.

---

# 6. LangSmith

## 6.1 LangSmith란?

LangSmith는 LLM 애플리케이션의 **실행 과정과 결과를 관찰하고 디버깅하기 위한 플랫폼**이다.

LangChain으로 AI 서비스를 개발하다 보면 다음과 같은 문제가 발생할 수 있다.

```text
Prompt가 제대로 전달되었는가?
       ↓
LLM이 어떤 입력을 받았는가?
       ↓
어떤 결과를 반환했는가?
       ↓
Chain의 어느 부분에서 문제가 발생했는가?
```

LangSmith를 이용하면 이러한 실행 과정을 추적하고 분석할 수 있다.

---

## 6.2 LangSmith의 주요 활용

```text
LangChain
    ↓
LLM 실행
    ↓
LangSmith
    ↓
실행 과정 추적
```

주요 기능:

- LLM 호출 추적
- 입력과 출력 확인
- Chain 실행 과정 확인
- 실행 시간 확인
- 오류 확인
- 애플리케이션 디버깅
- LLM 애플리케이션 성능 및 품질 분석

---

## 6.3 LangChain과 LangSmith

둘은 역할이 다르다.

| 구분 | 역할 |
|---|---|
| LangChain | LLM 애플리케이션 구성 및 실행 |
| LangSmith | LLM 애플리케이션 관찰, 추적, 디버깅 |

쉽게 생각하면:

```text
LangChain
→ AI 서비스를 만든다.

LangSmith
→ AI 서비스가 어떻게 동작하는지 확인한다.
```

---

# 7. 멀티모달(Multimodal)

## 7.1 멀티모달이란?

멀티모달은 **여러 종류의 데이터를 함께 이해하고 처리하는 것**을 의미한다.

대표적인 모달리티:

- 텍스트(Text)
- 이미지(Image)
- 음성(Audio)
- 영상(Video)

기존의 텍스트 기반 LLM이 텍스트만 처리했다면, 멀티모달 모델은 이미지 등의 다른 데이터를 함께 처리할 수 있다.

---

## 7.2 텍스트 + 이미지

예를 들어 이미지와 질문을 함께 전달할 수 있다.

```text
┌─────────────┐
│   이미지    │
└──────┬──────┘
       │
       ├──────────┐
       │          ↓
       │       멀티모달 LLM
       │          ↑
       └──── 질문 ┘
                  ↓
                답변
```

예:

```text
[사진]
      +
"이 사진에 무엇이 있나요?"
      ↓
AI
      ↓
"사진에는 강아지가 있습니다."
```

---

## 7.3 멀티모달의 활용

멀티모달 AI는 다양한 분야에서 활용할 수 있다.

- 이미지 분석
- 이미지 기반 질의응답
- 문서 및 PDF 분석
- 이미지 캡셔닝
- OCR
- 음성 기반 AI
- 영상 분석
- AI Agent의 시각 정보 처리

---

# 8. 오늘의 핵심 정리

## LangChain

```text
invoke
→ 실행 후 결과를 한 번에 반환

stream
→ 결과를 chunk 단위로 실시간 반환

logprob
→ 모델이 토큰을 선택할 때의 로그 확률
```

## LangSmith

```text
LangChain으로 AI 서비스 구현
          ↓
      LangSmith
          ↓
실행 추적 / 디버깅 / 분석
```

## Multimodal

```text
Text
Image
Audio
Video
 ↓
여러 형태의 데이터를 이해하고 처리
```
