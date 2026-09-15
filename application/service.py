from api.exceptions import ReceiptExceptions, TicketNotFoundError
from application.factory import TicketFactory
from domain.ticket import Ticket
from infrastructure.receipt import ReceiptPrinter, ConsoleReceiptPrinter
from infrastructure.receipt import Receipt
from uuid import UUID, uuid4
from typing import Optional

from infrastructure.printers import ConsolePrinter


class CinemaService:

    def __init__(self, ticket_factory : TicketFactory, receipt_printer : Optional[ReceiptPrinter] = None) -> None:
        self.__ticket_factory = ticket_factory
        self.__receipt_printer = receipt_printer
        self.__receipts : dict[UUID, Receipt] = {}
        self.__tickets : dict[UUID, Ticket] = {}

    def purchase_tickets(
            self,
            user_id: UUID,
            seats: list[tuple[int, int]],
            age: int,
            vip_flag: bool
    ) -> Receipt:

        list_ticket = [self.__ticket_factory.create_ticket(user_id, seat[0], seat[1], age, vip_flag) for seat in seats]
        receipt = Receipt(user_id, list_ticket)

        self.__receipts[receipt.receipt_id] = receipt

        tickets: list[Ticket] = []
        for row, number in seats:
            ticket = self.__ticket_factory.create_ticket(user_id, row, number, age, vip_flag)
            tickets.append(ticket)


        for ticket in tickets:
            self.__tickets[ticket.id] = ticket

        if self.__receipt_printer:
            self.__receipt_printer.print_receipt(receipt)

        return receipt

    def get_receipt(self, receipt_id : UUID):
        receipt = self.__receipts.get(receipt_id)
        if not receipt:
            raise ReceiptExceptions(f"Чек с id: {receipt_id} не найден")  # ✅ Кастомное исключение
        return receipt


    def get_ticket(self, ticket_id : UUID):
        ticket = self.__tickets.get(ticket_id)
        if not ticket:
            raise TicketNotFoundError(f"Билет с id: {ticket_id} не найден")
        return ticket


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

