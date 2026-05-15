import sqlite3
import tkinter as tk
from tkinter import messagebox
import pyttsx3
DB_NAME = "reminder_buddy.db"
# Initialize text-to-speech engine
engine = pyttsx3.init()
# Function to add a reminder
def add_reminder():
    task = task_entry.get()
    time = time_entry.get()
    if not task or not time:
        messagebox.showwarning("Warning", "Task and Time cannot be empty!")
        return
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO reminders (task, time) VALUES (?, ?)", (task, time))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Reminder added successfully!")
        task_entry.delete(0, tk.END)
        time_entry.delete(0, tk.END)
        fetch_reminders()  # Refresh the list after adding
    except Exception as e:
        messagebox.showerror("Error", f"Failed to add reminder: {str(e)}")
# Function to fetch all reminders and display them
def fetch_reminders():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM reminders")
        reminders = cursor.fetchall()
        conn.close()
        reminder_list.delete(0, tk.END)  # Clear listbox
        for r in reminders:
            reminder_list.insert(tk.END, f"{r[0]}. {r[1]} - {r[2]}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch reminders: {str(e)}")
# Function to delete a selected reminder
def delete_reminder():
    selected = reminder_list.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Please select a reminder to delete.")
        return
    reminder_text = reminder_list.get(selected[0])
    reminder_id = reminder_text.split(".")[0]
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM reminders WHERE id = ?", (reminder_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Reminder deleted successfully!")
        fetch_reminders()  # Refresh the list
    except Exception as e:
        messagebox.showerror("Error", f"Failed to delete reminder: {str(e)}")
# Function to read the selected reminder aloud
def read_reminder():
    selected = reminder_list.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Please select a reminder to read.")
        return
    reminder_text = reminder_list.get(selected[0]).split(". ", 1)[1]  # Extract task and time
    engine.say(reminder_text)
    engine.runAndWait()
# GUI Setup
root = tk.Tk()
root.title("Reminder Buddy")
# Task Input
tk.Label(root, text="Task:").grid(row=0, column=0, padx=5, pady=5)
task_entry = tk.Entry(root, width=30)
task_entry.grid(row=0, column=1, padx=5, pady=5)
# Time Input
tk.Label(root, text="Time (HH:MM):").grid(row=1, column=0, padx=5, pady=5)
time_entry = tk.Entry(root, width=15)
time_entry.grid(row=1, column=1, padx=5, pady=5)
# Buttons
tk.Button(root, text="Add Reminder", command=add_reminder).grid(row=2, column=0, columnspan=2, pady=5)
tk.Button(root, text="Read Reminder", command=read_reminder).grid(row=3, column=0, columnspan=2, pady=5)
tk.Button(root, text="Delete Reminder", command=delete_reminder).grid(row=4, column=0, columnspan=2, pady=5)
# Reminder Listbox
reminder_list = tk.Listbox(root, width=50, height=10)
reminder_list.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
# Fetch existing reminders on startup
fetch_reminders()
# Run GUI
root.mainloop()
