from fastapi import APIRouter, Depends, HTTPException
from api.dependencies import get_cinema_service
from api.shemas import ReceiptResponse, PurchaseRequest, TicketResponse
from application.service import CinemaService, receipt

from uuid import UUID

ticket_router = APIRouter(prefix = "/tickets")

@ticket_router.post("/purchase")
def ticket_buy(request : PurchaseRequest, service = Depends(get_cinema_service)) -> ReceiptResponse:

    purchase = service.purchase_tickets(
        request.user_id,
        request.seats,
        request.age,
        request.vip_flag
    )

    tickets_response = [
        TicketResponse(
            ticket_id=ticket.id,
            ticket_type=ticket.get_ticket_type(),  # Вызываем метод явно!
            row=ticket.row,
            number=ticket.number,
            price=ticket.price
        )
        for ticket in purchase.tickets
    ]


    receipt = ReceiptResponse(
        receipt_id=purchase.receipt_id,
        user_id=purchase.user_id,
        tickets=tickets_response,
        total_amount=purchase.total_amount,
        created_at=purchase.created_at
    )



    return receipt




@ticket_router.get("/{receipt_id}")
def get_tickets(receipt_id : UUID, service : CinemaService = Depends(get_cinema_service)) -> ReceiptResponse:

    receipt = service.get_receipt(receipt_id)

    if not receipt:
        raise HTTPException(status_code=404, detail="Чек не найден")

    tickets_response = [
        TicketResponse(
            ticket_id=ticket.id,
            ticket_type=ticket.get_ticket_type(),
            row=ticket.row,
            number=ticket.number,
            price=ticket.price
        )
        for ticket in receipt.tickets
    ]

    return ReceiptResponse(
        receipt_id = receipt.receipt_id,
        user_id = receipt.user_id,
        tickets = tickets_response,
        total_amount = receipt.total_amount,
        created_at = receipt.created_at
    )






