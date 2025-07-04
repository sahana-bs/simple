from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-001",
    temperature=2,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)
# test
messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    ("human", "This is my first langchain code, hurry"),
]
ai_msg = llm.invoke(messages)
ai_msg

print(ai_msg.content)

