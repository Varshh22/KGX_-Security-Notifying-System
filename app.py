from flask import Flask, request, render_template, redirect
from models import db, Attendance
from forms import AttendanceForm
from threading import Thread  # Import Thread
import generate_pdf
import email_service
import access_pass
from datetime import datetime
import subprocess
import threading
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attendance.db'  # Update if needed
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)

def run_scheduler():
    subprocess.run(["python", "scheduler.py"])
    
@app.route('/')
def index():
    form = AttendanceForm()
    return render_template('form.html', form=form)

@app.route('/submit', methods=['POST'])
def submit():
    form = AttendanceForm(request.form)
    if form.validate_on_submit():
        new_entry = Attendance(
            name=form.name.data,
            department=form.department.data,
            purpose=form.purpose.data,
            entry_time=form.entry_time.data,
            exit_time=form.exit_time.data,
            date_submitted=datetime.utcnow()
        )
        db.session.add(new_entry)
        db.session.commit()
        
        # Generate PDF and send email
        pdf_filename = generate_pdf.generate_pdf([new_entry])  # Pass as a list
        #email_service.send_email(pdf_filename)
        
        # Generate and send access pass
        access_pass.send_access_pass(new_entry)
        
        return redirect('/')
    return render_template('form.html', form=form)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.start()
    app.run(debug=True)
