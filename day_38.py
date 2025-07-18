# Day 38 of python with programming paglu🎀

#  What we'll Learn
# What is smtplib and how it works

# Send email via Gmail using Python

# Customize subject, body, and sender

# Add attachments (optional)


import smtplib
from email.message import EmailMessage

# Set up the email details
email = EmailMessage()
email['From'] = "reetutiwari1075@gmail.com"
email['To'] = "shivatiwari7171@gmail.com"
email['Subject'] = "Hello from shiva!"

# Email body
email.set_content("This is a test email sent using Python! 🚀")

# Gmail SMTP setup
def send_email():
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login("your_email@gmail.com", "your_app_password")
            smtp.send_message(email)
            print("✅ Email sent successfully!")
    except Exception as e:
        print("❌ Failed to send email:", e)

send_email()

# extra
# # Add attachment
# with open("file.txt", "rb") as f:
#     file_data = f.read()
#     file_name = f.name

# email.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)
