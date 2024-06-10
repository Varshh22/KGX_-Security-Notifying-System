import schedule
import time
from models import db, Attendance
import generate_pdf
import email_service
from flask import Flask
import os
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attendance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Function to check if tomorrow is a public holiday
def is_tomorrow_public_holiday():
    # Add logic to check if tomorrow is a public holiday
    # Example list of public holidays (dates should be in 'YYYY-MM-DD' format)
    public_holidays = [
        "2024-06-11",
         # Republic Day
        "2024-08-15",  # Independence Day
        "2024-10-02",  # Gandhi Jayanti
        # Add more dates here...
    ]
    tomorrow = datetime.now().date() + timedelta(days=1)
    return tomorrow.strftime('%Y-%m-%d') in public_holidays

def job():
    if is_tomorrow_public_holiday():
        with app.app_context():
            data = Attendance.query.all()
            pdf_filename = generate_pdf.generate_pdf(data)
            email_service.send_email(pdf_filename)

# Schedule the job to run daily at a specific time
schedule_time = "20:23"  # Set the time you want the job to run
schedule.every().day.at(schedule_time).do(job)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    while True:
        schedule.run_pending()
        time.sleep(1)
