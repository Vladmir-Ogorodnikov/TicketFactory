from functools import lru_cache

from application.factory import TicketFactory
from application.service import CinemaService
from infrastructure.printers import ConsolePrinter
from infrastructure.receipt import ConsoleReceiptPrinter
from functools import lru_cache


@lru_cache
def get_cinema_service() -> CinemaService:

    printer = ConsolePrinter()
    factory = TicketFactory(printer)
    receipt_printer = ConsoleReceiptPrinter()
    return CinemaService(factory, receipt_printer)
