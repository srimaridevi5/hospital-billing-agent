from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.bill import Bill
from fastapi.responses import FileResponse
import os
router = APIRouter(
    prefix="/bills",
    tags=["Bills"],
)


@router.get("/")
def get_all_bills(
    db: Session = Depends(get_db),
):
    bills = db.query(Bill).all()

    response = []

    for bill in bills:

        response.append(
            {
                "id": str(bill.id),
                "invoice_number": bill.invoice_number,
                "invoice_pdf": bill.invoice_pdf,
                "subtotal": float(bill.subtotal),
                "tax": float(bill.tax),
                "total": float(bill.total),
                "created_at": bill.created_at,
            }
        )

    return response


@router.get("/{bill_id}")
def get_bill(
    bill_id: UUID,
    db: Session = Depends(get_db),
):

    bill = (
        db.query(Bill)
        .filter(Bill.id == bill_id)
        .first()
    )

    if bill is None:
        raise HTTPException(
            status_code=404,
            detail="Bill not found",
        )

    return {
        "id": str(bill.id),
        "invoice_number": bill.invoice_number,
        "invoice_pdf": bill.invoice_pdf,
        "subtotal": float(bill.subtotal),
        "tax": float(bill.tax),
        "total": float(bill.total),
        "created_at": bill.created_at,
        "items": [
            {
                "service_name": item.service_name,
                "quantity": item.quantity,
                "unit_price": float(item.unit_price),
                "total_price": float(item.total_price),
            }
            for item in bill.items
        ],
    }


@router.get("/patient/{patient_id}")
def get_patient_bills(
    patient_id: UUID,
    db: Session = Depends(get_db),
):

    bills = (
        db.query(Bill)
        .filter(Bill.patient_id == patient_id)
        .all()
    )

    return [
        {
            "invoice_number": bill.invoice_number,
            "total": float(bill.total),
            "created_at": bill.created_at,
        }
        for bill in bills
    ]
@router.get("/download/{invoice_number}")
def download_invoice(invoice_number: str):

    filename = f"{invoice_number}.pdf"

    filepath = os.path.join(
        "generated_invoices",
        filename,
    )

    if not os.path.exists(filepath):
        raise HTTPException(
            status_code=404,
            detail="Invoice PDF not found.",
        )

    return FileResponse(
        path=filepath,
        media_type="application/pdf",
        filename=filename,
    )