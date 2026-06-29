import json
from pathlib import Path

from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.service_catalog import ServiceCatalog


def seed_service_catalog():
    db: Session = SessionLocal()

    json_path = Path(__file__).parent / "service_catalog.json"

    with open(json_path, "r", encoding="utf-8") as f:
        services = json.load(f)

    for service in services:
        exists = (
            db.query(ServiceCatalog)
            .filter(
                ServiceCatalog.service_code == service["service_code"]
            )
            .first()
        )

        if exists:
            continue

        db.add(
            ServiceCatalog(
                service_code=service["service_code"],
                service_name=service["service_name"],
                category=service["category"],
                unit_price=service["unit_price"],
            )
        )

    db.commit()
    db.close()

    print("Service catalog seeded successfully.")


if __name__ == "__main__":
    seed_service_catalog()