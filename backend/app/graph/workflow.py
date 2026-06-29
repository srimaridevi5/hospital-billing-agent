from langgraph.graph import StateGraph, START, END

from app.graph.state import BillingState

from app.agents.medical_agent import medical_agent
from app.agents.billing_agent import billing_agent
from app.services.invoice_service import generate_invoice


# Create Graph
builder = StateGraph(BillingState)


# -----------------------------
# Nodes
# -----------------------------
builder.add_node(
    "medical_agent",
    medical_agent,
)

builder.add_node(
    "billing_agent",
    billing_agent,
)

builder.add_node(
    "invoice",
    generate_invoice,
)


# -----------------------------
# Workflow
# -----------------------------
builder.add_edge(
    START,
    "medical_agent",
)

builder.add_edge(
    "medical_agent",
    "billing_agent",
)

builder.add_edge(
    "billing_agent",
    "invoice",
)

builder.add_edge(
    "invoice",
    END,
)


# -----------------------------
# Compile
# -----------------------------
billing_graph = builder.compile()