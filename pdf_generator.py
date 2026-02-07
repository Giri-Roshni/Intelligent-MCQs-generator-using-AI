from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf(mcqs_text, filename="Generated_MCQs.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    y = height - 50

    for line in mcqs_text.split("\n"):
        if y < 50:
            c.showPage()
            y = height - 50
        c.drawString(50, y, line)
        y -= 15

    c.save()
    return filename
