from pydantic import BaseModel, field_validator, Field
from uuid import UUID
from typing import List, Tuple
from domain.ticket import Ticket

class TicketResponse(BaseModel):
    """Pydantic схема для билета в ответе."""
    model_config = {"from_attributes": True}
    ticket_id: UUID
    ticket_type: str
    row: int
    number: int
    price: float

class PurchaseRequest(BaseModel):

    user_id : UUID
    seats: List[Tuple[int, int]]
    age : int
    vip_flag : bool

    @field_validator("age")
    @classmethod
    def validate_age(cls, v):
        if v <= 0:
            raise ValueError()
        return v

    @field_validator("seats")
    @classmethod
    def validate_seats(cls, seats):
        if not seats:
            raise ValueError()
        for row, number in seats:
            if row < 1 or number < 1:
                raise ValueError()
        return seats




class ReceiptResponse(BaseModel):
    model_config = {"from_attributes": True}
    receipt_id: UUID
    user_id : UUID
    tickets : List[TicketResponse]
    total_amount : float
    created_at : str
