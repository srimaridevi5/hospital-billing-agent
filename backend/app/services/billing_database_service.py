from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.bill import Bill
from app.models.bill_item import BillItem
from app.models.patient import Patient
from app.models.user import User


def save_bill(state):

    print("===== SAVE BILL CALLED =====")

    db: Session = SessionLocal()

    try:

        user = db.query(User).first()

        if user is None:
            raise Exception("No users found.")

        patient = (
            db.query(Patient)
            .filter(
                Patient.full_name == state["patient"]["name"]
            )
            .first()
        )

        if patient is None:

            patient = Patient(
                patient_number="PAT-" + state["invoice_number"][-8:],
                full_name=state["patient"]["name"],
                age=int(state["patient"]["age"]),
                gender=state["patient"]["gender"],
                created_by_id=user.id,
            )

            db.add(patient)
            db.flush()

            print("Patient created.")

        bill = Bill(
            patient_id=patient.id,
            invoice_number=state["invoice_number"],
            invoice_pdf=state["invoice_pdf"],
            subtotal=state["subtotal"],
            tax=state["tax"],
            total=state["total"],
        )

        db.add(bill)
        db.flush()

        print("Bill created.")

        for item in state["bill_items"]:

            db.add(
                BillItem(
                    bill_id=bill.id,
                    service_name=item["name"],
                    quantity=1,
                    unit_price=item["price"],
                    total_price=item["price"],
                )
            )

        print("Bill Items created.")

        db.commit()

        print("DATABASE COMMIT SUCCESS")

    except Exception as e:

        db.rollback()

        print("DATABASE ERROR")
        print(e)

        raise

    finally:

        db.close()