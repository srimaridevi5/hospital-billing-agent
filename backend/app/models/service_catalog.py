from sqlalchemy import Column, Integer, String, Float

from app.models.base import Base


class ServiceCatalog(Base):
    __tablename__ = "service_catalog"

    id = Column(Integer, primary_key=True, index=True)

    service_name = Column(String, unique=True, nullable=False)

    category = Column(String)

    department = Column(String)

    price = Column(Float)

    gst = Column(Float, default=18)