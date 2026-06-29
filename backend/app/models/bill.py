import uuid
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Bill(Base):
    __tablename__ = "bills"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )

    patient_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("patients.id"),
        nullable=False,
    )

    invoice_number: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )

    invoice_pdf: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    subtotal: Mapped[float] = mapped_column(
        Numeric(10, 2),
        default=0,
    )

    tax: Mapped[float] = mapped_column(
        Numeric(10, 2),
        default=0,
    )

    total: Mapped[float] = mapped_column(
        Numeric(10, 2),
        default=0,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    patient = relationship("Patient")

    items = relationship(
        "BillItem",
        back_populates="bill",
        cascade="all, delete-orphan",
    )