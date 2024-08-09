from uuid import UUID
from uuid import uuid4

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import UUID
from sqlalchemy import DateTime
from sqlalchemy.sql import func

from core.config import settings


class ProductModel(settings.DBBaseModel):
    __tablename__ = 'product'

    product_id = Column(UUID(as_uuid=True), default=uuid4, unique=True, primary_key=True)
    name = Column(String(256), nullable=False)
    category = Column(String(256), nullable=False)
    value = Column(Float(), nullable=False)
    created_on = Column(DateTime(timezone=True), server_default=func.now())
    updated_on = Column(DateTime(timezone=True), onupdate=func.now())
