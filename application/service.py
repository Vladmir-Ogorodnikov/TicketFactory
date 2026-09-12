from application.factory import TicketFactory
from infrastructure.receipt import ReceiptPrinter, ConsoleReceiptPrinter
from infrastructure.receipt import Receipt
from uuid import UUID, uuid4
from typing import Optional

from infrastructure.printers import ConsolePrinter


class CinemaService:

    def __init__(self, ticket_factory : TicketFactory, receipt_printer : Optional[ReceiptPrinter] = None) -> None:
        self.__ticket_factory = ticket_factory
        self.__receipt_printer = receipt_printer

    def purchase_tickets(
            self,
            user_id: UUID,
            seats: list[tuple[int, int]],
            age: int,
            vip_flag: bool
    ) -> Receipt:

        list_ticket = [self.__ticket_factory.create_ticket(user_id, seat[0], seat[1], age, vip_flag) for seat in seats]
        receipt = Receipt(user_id, list_ticket)

        if self.__receipt_printer:
            self.__receipt_printer.print_receipt(receipt)

        return receipt

ticket_printer = ConsolePrinter()
ticket_factory = TicketFactory(ticket_printer)
receipt_printer = ConsoleReceiptPrinter()
cinema_service = CinemaService(ticket_factory, receipt_printer)

# Покупка билетов
user_id = uuid4()
receipt = cinema_service.purchase_tickets(
    user_id=user_id,
    seats=[(1, 5), (1, 6), (2, 3)],
    age=25,
    vip_flag=False
)

print(f"Общая сумма: {receipt.total_amount}$")
print(f"Количество билетов: {len(receipt.tickets)}")

