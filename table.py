import sqlite3
conn = sqlite3.connect("reminder_buddy.db")  # Ensure this is the correct file
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS reminders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    time TEXT NOT NULL
)
""")
conn.commit()
conn.close()
print("✅ Table created successfully!")
