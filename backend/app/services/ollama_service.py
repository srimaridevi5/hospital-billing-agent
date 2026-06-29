from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2",
    base_url="http://127.0.0.1:11434",
    temperature=0,
)

def ask_llm(prompt: str):
    response = llm.invoke(prompt)
    return response.content