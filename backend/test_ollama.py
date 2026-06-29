from app.services.ollama_service import ask_llm

print(
    ask_llm(
        "Reply with exactly one word: Hello"
    )
)