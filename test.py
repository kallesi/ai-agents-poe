import openai

client = openai.OpenAI(
    api_key="anything",
    base_url="http://127.0.0.1:8000/v1/",
    default_headers={"Authorization": "Bearer anything"},
)

stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "this is a test request, write a short poem"}
    ],
    stream=True,
)

for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="", flush=True)
