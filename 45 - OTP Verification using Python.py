import os
import math
import random
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

OTP = "".join(random.choices("0123456789", k=6))

SENDER_EMAIL = "kunal749106@gmail.com"
APP_PASSWORD = "blwe wjsx zshg nvzp"

reciever = input("Enter your Email: ")
message = f"""Subject: OTP Verification

Your OTP is : {OTP}

This OTP is valid for  2 minutes."""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(SENDER_EMAIL,APP_PASSWORD)
server.sendmail(SENDER_EMAIL, reciever, message)
server.quit()

print("📩 OTP sent successfully")

# OTP validation
start_time = time.time()
user_otp = input("Enter your OTP: ")

if time.time() - start_time > 120:
    print("❌ OTP expired")
elif user_otp == OTP:
    print("✅ Verified")
else:
    print("❌ Invalid OTP")