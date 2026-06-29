import uuid

from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.patient import Patient
from app.models.user import User


def get_or_create_patient(state):

    db: Session = SessionLocal()

    try:
        # Check if patient already exists
        patient = (
            db.query(Patient)
            .filter(Patient.full_name == state.patient["name"])
            .first()
        )

        if patient:
            return patient

        # Get the first registered user
        user = db.query(User).first()

        if user is None:
            raise Exception("No users found.")

        # Create new patient
        patient = Patient(
            patient_number=f"PAT-{uuid.uuid4().hex[:8].upper()}",
            full_name=state.patient["name"],
            age=int(state.patient["age"]),
            gender=state.patient["gender"],
            created_by_id=user.id,
        )

        db.add(patient)
        db.commit()
        db.refresh(patient)

        return patient

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()