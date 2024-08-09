from datetime import datetime

from uuid import UUID

from typing import Optional

from pydantic import BaseModel


class BaseProductSchema(BaseModel):
    name: str
    category: str
    value: float


class GetProductSchema(BaseProductSchema):
    product_id: UUID
    created_on: datetime
    updated_on: Optional[datetime] = None