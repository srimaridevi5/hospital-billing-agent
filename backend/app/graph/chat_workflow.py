from langgraph.graph import StateGraph
from typing import TypedDict


class ChatState(TypedDict):

    question: str

    context: str

    answer: str


builder = StateGraph(ChatState)

chat_graph = builder.compile()