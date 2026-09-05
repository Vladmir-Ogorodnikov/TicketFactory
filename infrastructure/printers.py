from domain.ticket import Ticket
import os
import datetime
from typing import Protocol


class TicketPrinter(Protocol):

    def print_ticket(self, ticket : Ticket) -> None:
        ...


class ConsolePrinter:

    def print_ticket(self, ticket: Ticket) -> None:
        print("Билет\n"
              f"ID : {ticket.id}\n"
              f"Row: {ticket.row}\n"
              f"Number : {ticket.number}")


class PDFPrinter:

    def __init__(self, output_dir: str = "./tickets") -> None:
        self._output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def print_ticket(self, ticket: Ticket) -> str:
        filename = f"ticket_{ticket.id}.html"
        filepath = os.path.join(self._output_dir, filename)

        html_content = self._generate_html(ticket)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html_content)

        return filepath

    def _generate_html(self, ticket: Ticket) -> str:
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
        """.format(ticket_id=ticket.id, row=ticket.row, number=ticket.number, price=ticket.price,
                   created_at=datetime.datetime.now())

        return html_output