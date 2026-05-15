import sqlite3
import time
import pyttsx3
from datetime import datetime
# Initialize text-to-speech engine
engine = pyttsx3.init()
# Function to fetch reminders
def get_reminders():
    conn = sqlite3.connect("reminder_buddy.db")
    cursor = conn.cursor()
    now = datetime.now().strftime("%H:%M")
    cursor.execute("SELECT task FROM reminders WHERE time = ?", (now,))
    tasks = cursor.fetchall()
    conn.close()
    return tasks
# Continuous loop to check for reminders
print("🔄 Reminder system started... Checking for reminders.")
while True:
    reminders = get_reminders()
    if reminders:
        for task in reminders:
            print(f"🔔 Reminder: {task[0]}")
            engine.say(f"Reminder: {task[0]}")
            engine.runAndWait()
    time.sleep(10)  # Check every 10 seconds
