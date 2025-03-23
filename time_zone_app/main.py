import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

# Define available time zones
TIME_ZONES = [
    "UTC", "Asia/Karachi", "America/New_York", "Europe/London",
    "Asia/Tokyo", "Australia/Sydney", "America/Los_Angeles", "Europe/Berlin",
    "Asia/Dubai", "Asia/Kolkata"
]

# App title
st.title("🌍 Time Zone Converter")

# Multi-select dropdown for selecting time zones
selected_timezones = st.multiselect(
    "Select Timezones to Display Current Time:", TIME_ZONES, default=["UTC", "Asia/Karachi"]
)

# Display current time for selected time zones
if selected_timezones:
    st.subheader("Current Time in Selected Timezones")
    for tz in selected_timezones:
        current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
        st.write(f"**{tz}**: {current_time}")

# Time conversion section
st.subheader("⏳ Convert Time Between Timezones")

# Time input field with current time as default
input_time = st.time_input("Select Time:", value=datetime.now().time())

# Dropdowns for selecting source and target timezones
from_tz = st.selectbox("From Timezone:", TIME_ZONES, index=0)
to_tz = st.selectbox("To Timezone:", TIME_ZONES, index=1)

# Convert time button
if st.button("Convert Time"):
    # Combine today's date with selected time and source timezone
    dt = datetime.combine(datetime.today(), input_time, tzinfo=ZoneInfo(from_tz))
    # Convert time to target timezone
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    # Display the converted time
    st.success(f"⏰ Converted Time in {to_tz}: {converted_time}")
