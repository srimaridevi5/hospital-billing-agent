import uuid
import datetime

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import String, Text

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base import Base


class MedicalRecord(Base):

    __tablename__ = "medical_records"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )

    patient_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("patients.id")
    )

    uploaded_file: Mapped[str] = mapped_column(
        String(500)
    )

    extracted_json: Mapped[str] = mapped_column(
    Text,
    nullable=True,
)

    uploaded_at: Mapped[datetime.datetime] = mapped_column(
        DateTime,
        default=datetime.datetime.utcnow,
    )

    patient = relationship(
        "Patient",
        back_populates="medical_records"
    )