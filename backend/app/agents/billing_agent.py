from app.graph.state import BillingState
from app.services.service_catalog_service import get_service_price


def billing_agent(state: BillingState):

    items = []
    subtotal = 0

    for procedure in state["procedures"]:
        name = procedure["name"]
        price = get_service_price(name)

        items.append({
            "name": name,
            "price": price
        })

        subtotal += price

    for medicine in state["medicines"]:
        name = medicine["name"]
        price = get_service_price(name)

        items.append({
            "name": name,
            "price": price
        })

        subtotal += price

    for test in state["lab_tests"]:
        name = test["name"]
        price = get_service_price(name)

        items.append({
            "name": name,
            "price": price
        })

        subtotal += price

    tax = subtotal * 0.18
    total = subtotal + tax

    state["bill_items"] = items
    state["subtotal"] = subtotal
    state["tax"] = tax
    state["total"] = total
    state["status"] = "BILL_COMPLETED"

    return state