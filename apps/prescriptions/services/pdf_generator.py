from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML
from django.conf import settings


def generate_consultation_pdf(*, context: dict) -> HttpResponse:
    """
    Generate consultation PDF from HTML template and context.
    """

    html_string = render_to_string(
        "pdfs/consultation.html",
        context
    )

    html = HTML(
        string=html_string,
        base_url=settings.BASE_DIR
    )

    pdf_bytes = html.write_pdf()

    response = HttpResponse(
        pdf_bytes,
        content_type="application/pdf"
    )

    response["Content-Disposition"] = (
        'inline; filename="consultation.pdf"'
    )

    return response
