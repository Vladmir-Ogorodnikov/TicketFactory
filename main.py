from uuid import uuid4
from infrastructure.printers import ConsolePrinter, PDFPrinter
from application.factory import TicketFactory

printer = ConsolePrinter()
factory = TicketFactory(printer)
ticket = factory.create_ticket(uuid4(), 1, 5, 25, False)
print(ticket.get_info())


printer = PDFPrinter()
factory = TicketFactory(printer)
ticket = factory.create_ticket(uuid4(), 1, 5, 25, False)
print(ticket.get_info())