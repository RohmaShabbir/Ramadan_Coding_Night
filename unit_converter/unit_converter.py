import streamlit as st  # Import Streamlit for creating the web-based UI

# Function to convert units
def convert_units(value, unit_from, unit_to):
    conversions = {
        "meters_kilometers": 0.001,
        "kilometers_meters": 1000,
        "grams_kilograms": 0.001,
        "kilograms_grams": 1000,
        "celsius_fahrenheit": lambda c: (c * 9/5) + 32,
        "fahrenheit_celsius": lambda f: (f - 32) * 5/9,
    }

    key = f"{unit_from}_{unit_to}"
    
    if key in conversions:
        conversion = conversions[key]
        return conversion(value) if callable(conversion) else value * conversion
    elif unit_from == unit_to:
        return value  # If same units selected, return the same value
    else:
        return None  # Return None for unsupported conversions

# Streamlit UI setup
st.title("🌟 Smart Unit Converter")  
st.write("Convert between different units effortlessly!")

# User input
value = st.number_input("🔢 Enter value:", min_value=1.0, step=1.0)

# Dropdowns for unit selection
units = ["meters", "kilometers", "grams", "kilograms", "celsius", "fahrenheit"]
unit_from = st.selectbox("📌 Convert from:", units)
unit_to = st.selectbox("🎯 Convert to:", units)

# Convert button
if st.button("🔄 Convert"):
    result = convert_units(value, unit_from, unit_to)
    
    if result is not None:
        st.success(f"✅ Converted Value: {round(result, 4)} {unit_to}")
    else:
        st.error("❌ Conversion not supported. Please select valid units.")






# import streamlit as st  # Import Streamlit for creating the web-based UI


# # Function to convert units based on predefined conversion factors or formulas
# def convert_units(value, unit_from, unit_to):
#     conversions = {
#         "meters_kilometers": 0.001,  # 1 meter = 0.001 kilometers
#         "kilometers_meters": 1000,  # 1 kilometer = 1000 meters
#         "grams_kilograms": 0.001,  # 1 gram = 0.001 kilograms
#         "kilograms_grams": 1000,  # 1 kilogram = 1000 grams
#     }

#     key = f"{unit_from}_{unit_to}"  # Generate a key based on input and output units
#     if key in conversions:
#         conversion = conversions[key]
#         # If the conversion is a function (e.g., temperature conversion), call it
#         return (
#             conversion(value) if callable(conversion) else value * conversion
#         )  # Otherwise, multiply by the conversion factor
#     else:
#         return "Conversion not supported"  # Return message if conversion is not defined


# # Streamlit UI setup
# st.title("Unit Converter")  # Set title for the web app

# # User input: numerical value to convert
# value = st.number_input("Enter value:", min_value=1.0, step=1.0)

# # Dropdown to select unit to convert from
# unit_from = st.selectbox(
#     "Convert from:", ["meters", "kilometers", "grams", "kilograms"]
# )

# # Dropdown to select unit to convert to
# unit_to = st.selectbox(
#     "Convert to:", ["meters", "kilometers", "grams", "kilograms"]
# )

# # Button to trigger conversion
# if st.button("Convert"):
#     result = convert_units(value, unit_from, unit_to)  # Call the conversion function
#     st.write(f"Converted Value: {result}")  # Display the result