import os
from dotenv import load_dotenv
from google import genai

# .env 파일 로드
load_dotenv()

client = genai.Client()

# 목록에 존재하는 최신 모델 사용
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="안녕하세요! 자기소개 간단히 해주세요."
)

print(response.text)