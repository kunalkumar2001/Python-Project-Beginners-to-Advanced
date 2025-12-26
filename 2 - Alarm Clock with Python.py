from datetime import datetime
import os
from playsound import playsound
import time

alarm_time = input("Enter alarm time (HH:MM AM/PM): ")

time_part, period = alarm_time.split()
alarm_hour, alarm_minute = time_part.split(":")
period = period.upper()

print("Alarm set successfully!")

while True:
    now = datetime.now()

    if (now.strftime("%I") == alarm_hour and
        now.strftime("%M") == alarm_minute and
        now.strftime("%p") == period):
        print("⏰ Wake up!")
        playsound("alarm.wav")
        break

    time.sleep(1)
