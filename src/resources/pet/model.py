import uuid

from nguylinc_python_utils.sqlalchemy import BaseExtended
from sqlalchemy import Column, String, DateTime, UUID, ColumnElement

from src.init_models import Base


class Pet(Base, BaseExtended):
    __tablename__ = "pets"
    id = Column(UUID, primary_key=True, index=True, default=uuid.uuid4)
    created_at: ColumnElement = Column(DateTime(), index=True)
    name = Column(String(100))
    animal_type = Column(String(20))
    country = Column(String(20))
    editable_fields = ["name", "animal_type", "country"]
