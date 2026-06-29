from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.service_catalog import ServiceCatalog


def get_service_price(service_name: str):

    db: Session = SessionLocal()

    try:
        service = (
            db.query(ServiceCatalog)
            .filter(ServiceCatalog.service_name == service_name)
            .first()
        )

        if service:
            return float(service.price)

        return 0.0

    finally:
        db.close()