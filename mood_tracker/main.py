import streamlit as st  # For creating the web interface
import pandas as pd  # For data manipulation
import datetime  # For handling dates
import csv  # For reading and writing CSV files
import os  # For file operations

MOOD_FILE = "mood_log.csv"  # File to store mood log data

def load_mood_data():
    """Loads mood data from the CSV file if it exists, otherwise returns an empty DataFrame."""
    if not os.path.exists(MOOD_FILE) or os.stat(MOOD_FILE).st_size == 0:
        return pd.DataFrame(columns=["Date", "Mood"])
    
    return pd.read_csv(MOOD_FILE, encoding="utf-8")  # Reading CSV file and returning data

def save_mood_data(date, mood):
    """Saves the selected mood with the current date into the CSV file."""
    file_exists = os.path.exists(MOOD_FILE)  
    
    with open(MOOD_FILE, "a", newline="", encoding="utf-8") as file:  
        writer = csv.writer(file)
        if not file_exists or os.stat(MOOD_FILE).st_size == 0:
            writer.writerow(["Date", "Mood"])  # Writing header if file is newly created
        writer.writerow([str(date), mood])  # Writing mood entry

st.title("Mood Tracker 😊")  # Setting the title of the web app

today = datetime.date.today()  # Getting the current date

st.subheader("How are you feeling today?")  # Subheading for mood selection

mood = st.selectbox("Select your mood", ["Happy 😊", "Sad 😔", "Angry 😡", "Neutral 😇"])  # Dropdown menu for selecting mood

if st.button("Log Mood"):  # Button to log the selected mood
    save_mood_data(today, mood)  # Saving the selected mood to CSV file
    st.success("✅ Mood Logged Successfully!")  # Displaying success message

data = load_mood_data()  # Loading stored mood data

if not data.empty:  # Checking if data exists
    st.subheader("Mood Trends Over Time 📊")  # Subheading for mood trends
    
    data["Date"] = pd.to_datetime(data["Date"], errors='coerce')  # Converting date column to datetime format

    mood_counts = data["Mood"].value_counts()  # Counting occurrences of each mood

    st.bar_chart(mood_counts)  # Displaying mood trends as a bar chart
