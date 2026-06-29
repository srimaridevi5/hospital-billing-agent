import json

from app.graph.state import BillingState
from app.services.ollama_service import ask_llm


PROMPT = """
You are a hospital medical coding assistant.

Extract the following information.

Return ONLY valid JSON.

{
    "patient": {
        "name": "",
        "age": "",
        "gender": ""
    },
    "diagnosis": "",
    "procedures": [],
    "medications": [],
    "lab_tests": []
}
"""


def medical_agent(state: BillingState):

    prompt = f"""
{PROMPT}

Medical Record:

{state["extracted_text"]}
"""

    response = ask_llm(prompt)

    print("\n========== OLLAMA RAW RESPONSE ==========")
    print(response)
    print("=========================================\n")

    response = response.replace("```json", "")
    response = response.replace("```", "").strip()

    data = json.loads(response)

    state["patient"] = data.get("patient", {})

    state["diagnosis"] = data.get("diagnosis", "")

    state["procedures"] = [
        {"name": item}
        for item in data.get("procedures", [])
    ]

    state["medicines"] = [
        {"name": item}
        for item in data.get("medications", [])
    ]

    state["lab_tests"] = [
        {"name": item}
        for item in data.get("lab_tests", [])
    ]

    state["status"] = "MEDICAL_COMPLETED"

    return state