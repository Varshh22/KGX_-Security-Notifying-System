import schedule
import time
from models import db, Attendance
import generate_pdf
import email_service
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attendance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

def job():
    with app.app_context():
        data = Attendance.query.all()
        pdf_filename = generate_pdf.generate_pdf(data)
        email_service.send_email(pdf_filename)

# Schedule the job to run the day before each public holiday
# For demonstration purposes, we will schedule it to run every day at 18:00 (6 PM)
# schedule.every().day.at("15:10").do(job)
schedule.every().day.at("16:53").do(job)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
