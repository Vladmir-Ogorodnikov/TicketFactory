from infrastructure.printers import TicketPrinter
from uuid import UUID
from domain.ticket import ChildTicket, StandardTicket, VIPTicket, Ticket


class TicketFactory:

    def __init__(self, printer : TicketPrinter) -> None:
        self._printer = printer


    def create_ticket(self,user_id : UUID, row : int, number : int, age : int, vip_flag : bool) -> Ticket:
        if age < 12:
          current_ticket = ChildTicket(user_id, row, number)

        elif vip_flag:
            current_ticket = VIPTicket(user_id, row, number)
        else:
            current_ticket = StandardTicket(user_id, row, number)

        self._printer.print_ticket(current_ticket)
        return current_ticket