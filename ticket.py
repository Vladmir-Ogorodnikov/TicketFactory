import datetime
from abc import ABC, abstractmethod
from uuid import uuid4, UUID
from typing import Protocol
import os


class Ticket(ABC):

    def __init__(self, user_id, row, number, price):
        self.__id = uuid4()
        self.__user_id = user_id
        self.__row = row
        self.__number = number
        self.__price = price

    @property
    def id(self):
       return self.__id

    @property
    def row(self):
        return self.__row

    @property
    def number(self):
        return self.__number

    @property
    def price(self):
        return self.__price

    @abstractmethod
    def get_info(self):
        ...

class TicketPrinter(Protocol):

    def print_ticket(self, ticket : Ticket) -> None:
        ...

class ConsolePrinter:

    def print_ticket(self, ticket : Ticket) -> None:
        print("Билет\n"
              f"ID : {ticket.id}\n"
              f"Row: {ticket.row}\n"
              f"Number : {ticket.number}")

class PDFPrinter:

    def __init__(self, output_dir : str = "./tickets") -> None:
        self._output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def print_ticket(self, ticket: Ticket) -> str:

        filename = f"ticket_{ticket.id}.html"
        filepath = os.path.join(self._output_dir, filename)


        html_content = self._generate_html(ticket)


        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html_content)

        return filepath


    def _generate_html(self, ticket : Ticket) -> str:

        html_output = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Билет {ticket_id}</title>
            <style>
                body {{ font-family: Arial, sans-serif; padding: 20px; }}
                .ticket {{ border: 2px solid #333; padding: 20px; max-width: 400px; }}
                .header {{ background: #2c3e50; color: white; padding: 10px; text-align: center; }}
                .info {{ margin: 15px 0; }}
                .info-row {{ display: flex; justify-content: space-between; margin: 5px 0; }}
                .footer {{ border-top: 1px solid #ccc; padding-top: 10px; font-size: 12px; }}
            </style>
        </head>
        <body>
            <div class="ticket">
                <div class="header">
                    <h2>🎬 КИНОТЕАТР</h2>
                </div>
                <div class="info">
                    
                    <div class="info-row">
                        <strong>Ряд:</strong>
                        <span>{row}</span>
                    </div>
                    <div class="info-row">
                        <strong>Место:</strong>
                        <span>{number}</span>
                    </div>
                    <div class="info-row">
                        <strong>Цена:</strong>
                        <span>{price}$</span>
                    </div>
                </div>
                <div class="footer">
                    <p>ID билета: {ticket_id}</p>
                    <p>Дата создания: {created_at}</p>
                </div>
            </div>
        </body>
        </html>
        """.format(ticket_id = ticket.id, row = ticket.row, number = ticket.number, price = ticket.price, created_at = datetime.datetime.now())

        return html_output



class StandardTicket(Ticket):

    def __init__(self, user_id, row, number, price : int = 10):
        super().__init__(user_id, row, number, price)




    def get_info(self):
        return f"Стандартный билет, ряд {self.row}, место {self.number}, цена: {self.price}$"



class VIPTicket(Ticket):

    def __init__(self, user_id, row, number, price: int = 25):
        super().__init__(user_id, row, number, price)


    def get_info(self):
        return f"VIP-билет с баром, ряд {self.row}, место {self.number}, цена: {self.price}$"


class ChildTicket(Ticket):

    def __init__(self, user_id, row, number, price : int = 5):
        super().__init__(user_id, row, number, price)

    def get_info(self):
        return f"Детский билет, ряд {self.row}, место {self.number}, цена: {self.price}$"


class TicketFactory:

    def __init__(self, printer : TicketPrinter) -> None:
        self._printer = printer


    def create_ticket(self, user_id : UUID, row : int, number : int, age : int, vip_flag : bool) -> Ticket:
        if age < 12:
          current_ticket = ChildTicket(user_id, row, number)

        elif vip_flag:
            current_ticket = VIPTicket(user_id, row, number)
        else:
            current_ticket = StandardTicket(user_id, row, number)

        self._printer.print_ticket(current_ticket)
        return current_ticket

printer = ConsolePrinter()
factory = TicketFactory(printer)
ticket = factory.create_ticket(uuid4(), 1, 5, 25, False)
print(ticket.get_info())


printer = PDFPrinter()
factory = TicketFactory(printer)
ticket = factory.create_ticket(uuid4(), 1, 5, 25, False)
print(ticket.get_info())