
import openai
openai.api_key = "申请的AppId"
openai.api_base = ""

result = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "user", "content": "给我说两个科学家的名字"},
  ],
  stream=True
)
for chunk in result:
  print(chunk)
