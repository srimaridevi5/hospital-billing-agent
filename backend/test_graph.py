from app.graph.workflow import billing_graph
from app.graph.state import BillingState


state = BillingState(

    extracted_text="""

Patient Name : John Doe

Age : 45

Diagnosis :

Acute Appendicitis

Treatment :

Appendectomy Surgery

Medications :

Ceftriaxone

Paracetamol

Lab Tests :

CBC

Ultrasound Abdomen

"""
)

result = billing_graph.invoke(state)

print(result)