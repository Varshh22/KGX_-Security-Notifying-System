from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import datetime

def generate_pdf(data):
    filename = f"attendance_report_{datetime.date.today()}.pdf"
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    c.drawString(100, height - 100, "KGX Public Holiday Attendance Report")
    c.drawString(100, height - 120, f"Date: {datetime.date.today()}")
    
    y = height - 150
    for entry in data:
        text = f"Name: {entry.name}, Department: {entry.department}, Purpose: {entry.purpose}, Entry: {entry.entry_time}, Exit: {entry.exit_time}"
        c.drawString(100, y, text)
        y -= 20
    
    c.save()
    return filename
