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
<<<<<<< HEAD
    "2024-01-01",
    "2024-06-11",
    "2024-01-14",
    "2024-01-26",
    "2024-04-12",
    "2024-04-14",
    "2024-05-01",
    "2024-08-15",
    "2024-08-23",
    "2024-10-02",
    "2024-10-22",
    "2024-12-25",
    "2024-01-07", "2024-01-14", "2024-01-21", "2024-01-28",
    "2024-02-04", "2024-02-11", "2024-02-18", "2024-02-25",
    "2024-03-03", "2024-03-10", "2024-03-17", "2024-03-24", "2024-03-31",
    "2024-04-07", "2024-04-14", "2024-04-21", "2024-04-28",
    "2024-05-05", "2024-05-12", "2024-05-19", "2024-05-26",
    "2024-06-02", "2024-06-09", "2024-06-16", "2024-06-23", "2024-06-30",
    "2024-07-07", "2024-07-14", "2024-07-21", "2024-07-28",
    "2024-08-04", "2024-08-11", "2024-08-18", "2024-08-25",
    "2024-09-01", "2024-09-08", "2024-09-15", "2024-09-22", "2024-09-29",
    "2024-10-06", "2024-10-13", "2024-10-20", "2024-10-27",
    "2024-11-03", "2024-11-10", "2024-11-17", "2024-11-24",
    "2024-12-01", "2024-12-08", "2024-12-15", "2024-12-22", "2024-12-29",
]

=======
        "2024-06-11",  # Republic Day
        "2024-08-15",  # Independence Day
        "2024-10-02",  # Gandhi Jayanti
        # Add more dates here...
    ]
>>>>>>> main
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
<<<<<<< HEAD
schedule_time = "22:01"  # Set the time you want the job to run
=======
schedule_time = "21:25"  # Set the time you want the job to run
>>>>>>> main
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
