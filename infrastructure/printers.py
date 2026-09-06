from domain.ticket import Ticket
import os
import datetime
from typing import Protocol
from fpdf import FPDF




class TicketPrinter(Protocol):

    def print_ticket(self, ticket : Ticket) -> None:
        ...


class ConsolePrinter:

    def print_ticket(self, ticket: Ticket) -> None:
        print("Билет\n"
              f"ID : {ticket.id}\n"
              f"Row: {ticket.row}\n"
              f"Number : {ticket.number}")


class HTMLPrinter:

    def __init__(self, output_dir: str = "./tickets_html") -> None:
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

class PDFPrinter:

    def __init__(self, path : str = "./tickets_pdf") -> None:
        self._output_dir = path
        os.makedirs(path, exist_ok=True)

    def print_ticket(self, ticket : Ticket) -> None:

        filename = f"{ticket.id}.pdf"
        output_path = os.path.join(self._output_dir, filename)

        pdf = FPDF(unit='mm', format=(100, 100))
        pdf.set_margins(5, 5, 5)
        pdf.add_page()

        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, "Cinema", align='C')
        pdf.ln(12)

        # Разделитель
        pdf.set_draw_color(0, 0, 0)
        pdf.line(5, pdf.get_y(), 95, pdf.get_y())
        pdf.ln(5)

        pdf.set_font("Arial", "B", 11)
        pdf.cell(0, 8, f"ID ticket: {str(ticket.id)}")
        pdf.ln(8)
        pdf.cell(0, 8, f"Row: {str(ticket.row)}")
        pdf.ln(8)
        pdf.cell(0, 8, f"Number: {str(ticket.number)}")
        pdf.ln(8)
        pdf.cell(0, 8, f"Price: {str(ticket.price)}$")
        pdf.ln(8)
        pdf.set_font("Arial", "I", 9)
        pdf.cell(0, 8, f"Date: {str(datetime.datetime.now().strftime("%d.%m.%Y %H:%M"))}")
        pdf.output(output_path)
