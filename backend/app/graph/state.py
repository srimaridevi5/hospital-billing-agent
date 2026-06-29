from typing import TypedDict


class BillingState(TypedDict, total=False):

    extracted_text: str

    patient: dict

    diagnosis: str

    procedures: list

    medicines: list

    lab_tests: list

    bill_items: list

    subtotal: float

    tax: float

    total: float

    invoice_number: str

    invoice_pdf: str

    status: str

    # Chat

    question: str

    answer: str

    context: str

    question: str = ""

    chat_answer: str = ""

    chat_context: str = ""