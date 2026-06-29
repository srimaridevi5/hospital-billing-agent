from sqlalchemy.orm import Session

from app.models.patient import Patient
from app.models.bill import Bill
from app.models.bill_item import BillItem

from app.agents.chat_agent import chat_agent


class ChatService:

    @staticmethod
    def ask(
        db: Session,
        patient_name: str,
        question: str,
    ):

        patient = (
            db.query(Patient)
            .filter(
                Patient.full_name == patient_name
            )
            .first()
        )

        if patient is None:
            return "Patient not found."

        bill = (
            db.query(Bill)
            .filter(
                Bill.patient_id == patient.id
            )
            .first()
        )

        items = (
            db.query(BillItem)
            .filter(
                BillItem.bill_id == bill.id
            )
            .all()
        )

        context = f"""
Patient Name:
{patient.full_name}

Age:
{patient.age}

Gender:
{patient.gender}

Invoice:
{bill.invoice_number}

Subtotal:
{bill.subtotal}

GST:
{bill.tax}

Total:
{bill.total}

Bill Items:

"""

        for item in items:

            context += (
                f"{item.service_name}"
                f" - ₹{item.total_price}\n"
            )

        return chat_agent(
            question,
            context,
        )