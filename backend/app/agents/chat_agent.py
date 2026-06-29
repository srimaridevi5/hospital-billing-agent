from app.prompts.chat_prompt import CHAT_PROMPT
from app.services.ollama_service import ask_llm


def chat_agent(question: str, context: str):

    prompt = CHAT_PROMPT.format(
        context=context,
        question=question,
    )

    answer = ask_llm(prompt)

    answer = answer.replace("```", "").strip()

    return answer