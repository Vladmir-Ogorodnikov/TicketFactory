from uuid import uuid4, UUID
from typing import List
from domain.ticket import Ticket
import datetime


class Receipt:

    def __init__(self, user_id : UUID, tickets : List[Ticket]) -> None:
        self.__receipt_id = uuid4()
        self.__user_id = user_id
        self.total_amount = sum(ticket.price for ticket in tickets)
        self.__created_at = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
        self.__tickets = tickets

    @property
    def receipt_id(self):
        return self.__receipt_id

    @property
    def user_id(self):
        return self.__user_id

    @property
    def created_at(self):
        return self.__created_at

    @property
    def tickets(self):
        return self.__tickets


    def __data_string(self) -> str:

        group_tickets = {}

        for ticket in self.tickets:
            ticket_type = ticket.get_ticket_type()
            group_tickets[ticket_type] = group_tickets.get(ticket_type, 0) + 1


        result = [f"{ticket_type} x {count}" for ticket_type, count in group_tickets.items()]

        tickets_str = "\n".join(result)

        receipt = (f"ID: {self.receipt_id}\n"
                   f"Tickets:\n"
                   f"{tickets_str}\n"
                   f"Total amount : {self.total_amount}\n"
                   f"Date: {self.created_at}"
                   )
        return receipt


    def get_receipt_info(self) -> str:
        return self.__data_string()







