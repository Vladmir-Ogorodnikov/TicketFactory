class CinemaServiceExceptions(Exception):
    def __init__(self, name):
        self.name = name
        super().__init__(name)


class TicketExceptions(CinemaServiceExceptions):
    def __init__(self, name: str):
        super().__init__(name)

class ReceiptExceptions(CinemaServiceExceptions):
    def __init__(self, name: str):
        super().__init__(name)

class ReceiptNotFoundError(ReceiptExceptions):
    def __init__(self, name: str):
        super().__init__(name)

class TicketNotFoundError(TicketExceptions):
    def __init__(self, name: str):
        super().__init__(name)

class TicketValidationError(TicketExceptions):
    def __init__(self, name: str):
        super().__init__(name)

class EmptySeatsError(TicketExceptions):
    def __init__(self, name: str):
        super().__init__(name)

