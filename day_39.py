# Day 39 of Python with Programming Paglu 🎀

# Goal
# Read a CSV file with names + birthdays
# Check if today is anyone’s birthday
# Send them a Happy Birthday email automatically 🎉

import csv
from datetime import datetime
import smtplib
from email.message import EmailMessage

# Load today's date
today = datetime.now().strftime("%m-%d")

# Load birthday data from CSV
def get_birthdays_today():
    birthdays_today = []
    with open("birthdays.csv", newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            bday = datetime.strptime(row['birthday'], "%Y-%m-%d").strftime("%m-%d")
            if bday == today:
                birthdays_today.append(row)
    return birthdays_today

# Send email
def send_birthday_email(to_email, to_name):
    msg = EmailMessage()
    msg['Subject'] = "🎉 Happy Birthday!"
    msg['From'] = "shivatiwari7171@gmail.com"
    msg['To'] = to_email
    msg.set_content(f"Hey {to_name},\n\nWishing you a day filled with happiness and a year filled with joy. Happy Birthday! 🎂🥳")

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login("shivatiwari7171@gmail.com", "your_app_password")
            smtp.send_message(msg)
            print(f"✅ Sent birthday wish to {to_name}")
    except Exception as e:
        print(f"❌ Failed to send email to {to_name}: {e}")

# Run the reminder
birthdays = get_birthdays_today()
for person in birthdays:
    send_birthday_email(person['email'], person['name'])
