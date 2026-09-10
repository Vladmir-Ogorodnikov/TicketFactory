from pydantic import BaseModel
from uuid import UUID
from typing import List, Tuple
from domain.ticket import Ticket

class TicketResponse(BaseModel):
    """Pydantic схема для билета в ответе."""
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

class ReceiptResponse(BaseModel):
    ticket_id : UUID
    user_id : UUID
    tickets : List[TicketResponse]
    total_amount : float
    created_at : str
