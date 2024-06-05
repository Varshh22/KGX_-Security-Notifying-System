from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def send_access_pass(entry):
    filename = f"access_pass_{entry.name}_{entry.date_submitted}.pdf"
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    c.drawString(100, height - 100, "KGX Public Holiday Access Pass")
    c.drawString(100, height - 120, f"Name: {entry.name}")
    c.drawString(100, height - 140, f"Department: {entry.department}")
    c.drawString(100, height - 160, f"Purpose: {entry.purpose}")
    c.drawString(100, height - 180, f"Entry Time: {entry.entry_time}")
    c.drawString(100, height - 200, f"Exit Time: {entry.exit_time}")
    c.drawString(100, height - 220, f"Date Issued: {entry.date_submitted}")
    
    c.save()
    # Implement email or other delivery methods here
