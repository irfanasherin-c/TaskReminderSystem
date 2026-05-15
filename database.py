import sqlite3
DB_NAME = "reminder_buddy.db"
print("🚀 database.py is running...")  # Debugging print
# Function to create the table
def create_table():
    print("🛠 Creating/checking table...")  # Debugging print
    conn = sqlite3.connect(DB_NAME)
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
    print("✅ Table 'reminders' created/checked.")
# Function to fetch all reminders
def get_reminders():
    print("📌 Fetching reminders...")  # Debugging print
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reminders")
    reminders = cursor.fetchall()
    conn.close()
    if reminders:
        print("📌 Existing reminders in database:")
        for r in reminders:
            print(f"   - ID: {r[0]}, Task: {r[1]}, Time: {r[2]}")
    else:
        print("ℹ No reminders found in database.")
    return reminders
# Ensure the script runs operations when executed
if __name__ == "_main_":
    print("🔄 Running database setup...")  # Debugging print
    create_table()  # Ensure the table exists
    get_reminders()  # Fetch existing reminders
    print("🏁 database.py execution complete.")  # Debugging print
