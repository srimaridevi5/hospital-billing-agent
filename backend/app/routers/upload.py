import os
import uuid

from fastapi import APIRouter, UploadFile, File, HTTPException

from app.graph.workflow import billing_graph
from app.graph.state import BillingState
from app.services.pdf_service import extract_pdf_text
from app.services.billing_database_service import save_bill

router = APIRouter(
    prefix="/upload",
    tags=["Medical Records"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/")
async def upload_medical_record(
    file: UploadFile = File(...)
):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    filename = f"{uuid.uuid4()}.pdf"
    filepath = os.path.join(UPLOAD_DIR, filename)

    with open(filepath, "wb") as buffer:
        buffer.write(await file.read())

    extracted_text = extract_pdf_text(filepath)

    state = BillingState(
        extracted_text=extracted_text
    )

    result = billing_graph.invoke(state)

    print("========== GRAPH RESULT ==========")
    print(result)
    print("==================================")

    save_bill(result)

    return {
        "invoice_number": result["invoice_number"],
        "invoice_pdf": result["invoice_pdf"],
        "patient": result["patient"],
        "diagnosis": result["diagnosis"],
        "bill_items": result["bill_items"],
        "subtotal": result["subtotal"],
        "tax": result["tax"],
        "total": result["total"],
        "status": result["status"]
    }