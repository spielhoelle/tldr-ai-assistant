import sys
import requests
import os

query = sys.argv[1]

api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("MODEL_TYPE")

def chat_with_chatgpt(prompt):
    res = requests.post(
        f"https://api.openai.com/v1/chat/completions",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        json={
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 100,
        },
    ).json()
    return res["choices"][0]["message"]["content"]


promptWithQuery = (
    f'Summarize the text delimited by triple quotes in one sentence """{query}"""'
)
result = chat_with_chatgpt(promptWithQuery)
print(result)
