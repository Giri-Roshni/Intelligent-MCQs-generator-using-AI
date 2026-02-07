from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from textwrap import wrap

def generate_pdf(mcqs_text, filename="Generated_MCQs.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    x_margin = 50
    y_margin = 50
    max_chars = 90  # max chars per line

    text_object = c.beginText(x_margin, height - y_margin)
    text_object.setFont("Helvetica", 12)

    for line in mcqs_text.split("\n"):
        wrapped_lines = wrap(line, max_chars)

        if not wrapped_lines:
            text_object.textLine("")
        else:
            for wline in wrapped_lines:
                if text_object.getY() < y_margin:
                    c.drawText(text_object)
                    c.showPage()
                    text_object = c.beginText(x_margin, height - y_margin)
                    text_object.setFont("Helvetica", 12)
                text_object.textLine(wline)

    c.drawText(text_object)
    c.save()
    return filename
