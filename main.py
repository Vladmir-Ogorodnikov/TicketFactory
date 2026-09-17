
from uuid import uuid4
from infrastructure.printers import ConsolePrinter, PDFPrinter
from application.factory import TicketFactory
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from api.routes import ticket_router
from api.health import health_router
from api.exceptions import TicketExceptions, ReceiptExceptions, TicketValidationError
from infrastructure.receipt import Receipt
from uuid import UUID

app = FastAPI()
app.include_router(ticket_router)
app.include_router(health_router)

@app.exception_handler(TicketExceptions)
def ticket_exceptions(request : Request, exc : TicketExceptions):
    return JSONResponse(
        content={
            "Error": exc.name,
            "HOST": request.client.host
        },
        status_code = 400
    )

@app.exception_handler(ReceiptExceptions)
def receipt_exceptions(request : Request, exc : ReceiptExceptions):
    print(f"✅ ОБРАБОТЧИК ВЫЗВАН!")
    return JSONResponse(
        content = {
            "Error" : exc.name,
            "HOST" : request.client.host
        },
        status_code = 404
    )

@app.exception_handler(TicketValidationError)
def validation_exceptions(request : Request, exc : TicketValidationError):
    return JSONResponse(
        content={
            "Error": exc.name,
            "HOST": request.client.host
        },
        status_code = 422
    )


# printer = ConsolePrinter()
# factory = TicketFactory(printer)
# ticket = factory.create_ticket(uuid4(), 1, 5, 25, False)
# print(ticket.get_info())
#
#
# printer = PDFPrinter()
# factory = TicketFactory(printer)
# ticket = factory.create_ticket(uuid4(), 1, 5, 25, False)
# print(ticket.get_info())