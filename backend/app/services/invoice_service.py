import os
import uuid

from reportlab.pdfgen import canvas

OUTPUT_FOLDER = "generated_invoices"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def generate_invoice(state):

    invoice_number = f"INV-{uuid.uuid4().hex[:8].upper()}"

    filepath = os.path.join(
        OUTPUT_FOLDER,
        f"{invoice_number}.pdf",
    )

    c = canvas.Canvas(filepath)

    y = 800

    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, y, "ABC MULTISPECIALITY HOSPITAL")

    y -= 35

    c.setFont("Helvetica", 12)

    c.drawString(50, y, f"Invoice No : {invoice_number}")

    y -= 20

    c.drawString(
        50,
        y,
        f"Patient : {state['patient'].get('name', '')}",
    )

    y -= 20

    c.drawString(
        50,
        y,
        f"Age : {state['patient'].get('age', '')}",
    )

    y -= 20

    c.drawString(
        50,
        y,
        f"Gender : {state['patient'].get('gender', '')}",
    )

    y -= 30

    c.drawString(
        50,
        y,
        f"Diagnosis : {state['diagnosis']}",
    )

    y -= 40

    c.setFont("Helvetica-Bold", 13)
    c.drawString(50, y, "Bill Items")

    y -= 25

    c.setFont("Helvetica", 12)

    for item in state["bill_items"]:

        c.drawString(
            60,
            y,
            f"{item['name']}    ₹ {item['price']}",
        )

        y -= 20

    y -= 20

    c.drawString(
        50,
        y,
        f"Subtotal : ₹ {state['subtotal']}",
    )

    y -= 20

    c.drawString(
        50,
        y,
        f"GST : ₹ {state['tax']}",
    )

    y -= 20

    c.drawString(
        50,
        y,
        f"Grand Total : ₹ {state['total']}",
    )

    c.save()

    state["invoice_number"] = invoice_number
    state["invoice_pdf"] = filepath

    return state