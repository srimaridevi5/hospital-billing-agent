import uuid

from sqlalchemy import ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class BillItem(Base):
    __tablename__ = "bill_items"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )

    bill_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("bills.id"),
        nullable=False,
    )

    service_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    quantity: Mapped[int] = mapped_column(
        Integer,
        default=1,
    )

    unit_price: Mapped[float] = mapped_column(
        Numeric(10,2),
        nullable=False,
    )

    total_price: Mapped[float] = mapped_column(
        Numeric(10,2),
        nullable=False,
    )

    bill = relationship(
        "Bill",
        back_populates="items",
    )