from abc import ABC, abstractmethod
from uuid import uuid4

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