import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")

print("API Key 존재:", api_key is not None)

client = OpenAI()

response = client.responses.create(
    model="gpt-5-mini",
    input="API 연결 테스트입니다. '연결 성공'이라고만 답해주세요."
)

print(response.output_text)

# pip install openai python-dotenv
# from dotenv import load_dotenv
# import os
# from openai import OpenAI

# load_dotenv()

# api_key = os.getenv("OPENAI_API_KEY")

# print("API Key 존재:", bool(api_key))

# client = OpenAI()

# response = client.responses.create(
#     model="gpt-5-mini",
#     input="API 연결 테스트입니다."
# )

# print(response.output_text)