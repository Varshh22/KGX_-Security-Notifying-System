import schedule
import time
from models import db, Attendance
import generate_pdf
import email_service
from flask import Flask
from datetime import datetime, timedelta
import logging

# Initialize the Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attendance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to check if tomorrow is a public holiday
def is_tomorrow_public_holiday():
    public_holidays = [
        "2024-06-11",  # Republic Day
        "2024-08-15",  # Independence Day
        "2024-10-02",  # Gandhi Jayanti
        # Add more dates here...
    ]
    tomorrow = datetime.now().date() + timedelta(days=1)
    return tomorrow.strftime('%Y-%m-%d') in public_holidays

def job():
    if is_tomorrow_public_holiday():
        with app.app_context():
            logging.info('Public holiday detected. Generating PDF and sending email.')
            data = Attendance.query.all()
            pdf_filename = generate_pdf.generate_pdf(data)
            email_service.send_email(pdf_filename)
            logging.info(f'Email sent with attachment {pdf_filename}')
    else:
        logging.info('No public holiday tomorrow.')

# Schedule the job to run daily at a specific time
schedule_time = "21:25"  # Set the time you want the job to run
schedule.every().day.at(schedule_time).do(job)
logging.info(f'Scheduler set to run daily at {schedule_time}')

def run_scheduler():
    with app.app_context():
        db.create_all()
    
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info('Scheduler stopped.')

if __name__ == "__main__":
    run_scheduler()
