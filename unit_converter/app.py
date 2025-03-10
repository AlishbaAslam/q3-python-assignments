import streamlit as st

# Title and description of the app.
st.title("🔄Unit Converter (Unitify)")
st.markdown("#### Welcome! Simply choose a category, input your number, choose the desired units, and get accurate results in seconds! 🚀")

# Selecting a category.
category = st.selectbox("Select a category", ["Length", "Temperature", "Weight", "Time", "Area"])

# Length conversion.
if category == "Length":
    st.markdown("##### Length Conversion")
    input_value = st.number_input("Enter the Value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From Unit:", ["Meters", "Kilometers", "Foot", "Inches", "Centimeters", "Yards", "Miles"])
    to_unit = st.selectbox("To Unit:", ["Meters", "Kilometers", "Foot", "Inches", "Centimeters", "Yards", "Miles"])

    # Length Conversion Factors.
    length_conversion = {
        "Meters": 1, #Base Unit
        "Kilometers": 1000, #1 Kilometer is equal to 1000 Meters
        "Foot": 0.3048, #1 Foot is equal to 0.3048 Meters
        "Inches": 0.0254, #1 Inch is equal to 0.0254 Meters
        "Centimeters": 0.01, #1 Centimeter is equal to 0.01 Meters
        "Yards": 0.9144, #1 Yard is equal to 0.9144 Meters
        "Miles": 1609.34, #1 Mile is equal to 1609.34 Meters
    }

    # Length Conversion Logic.
    if st.button("Convert"):
        result = input_value * (length_conversion[from_unit] / length_conversion[to_unit])
        st.success(f"{input_value}  {from_unit} is equal to {result:.2f}  {to_unit}") #Like 1 Kilometer is equal to 1000 Meters.


# Weight conversion.
elif category == "Weight":
    st.markdown("##### Weight Conversion")
    input_value = st.number_input("Enter the Value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From Unit:", ["Kilograms", "Grams", "Pounds", "Ounces", "Tons", "Stone"])
    to_unit = st.selectbox("To Unit:", ["Kilograms", "Grams", "Pounds", "Ounces", "Tons", "Stone"])

    # Weight Conversion Factors.
    weight_conversion = {
        "Kilograms": 1, #Base Unit
        "Grams": 0.001, #1 Gram is equal to 0.001 Kilograms
        "Pounds": 0.453592, #1 Pound is equal to 0.453592 Kilograms
        "Ounces": 0.0283495, #1 Ounce is equal to 0.0283495 Kilograms
        "Tons": 1000, #1 Ton is equal to 1000 Kilograms
        "Stone": 6.35029, #1 Stone is equal to 6.35029 Kilograms
    }

    # Weight Conversion Logic.
    if st.button("Convert"):
        result = input_value * (weight_conversion[from_unit] / weight_conversion[to_unit])
        st.success(f"{input_value}  {from_unit} is equal to {result:.2f}  {to_unit}") #Like 1 Gram is equal to 0.001 Kilograms.


# Temperature conversion.
elif category == "Temperature":
    st.markdown("##### Temperature Conversion")
    input_value = st.number_input("Enter the Value:", format="%.2f")
    from_unit = st.selectbox("From Unit:", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To Unit:", ["Celsius", "Fahrenheit", "Kelvin"])
    
    # Temperature Conversion Logic.
    def temperature_conversion(value, from_unit, to_unit):
        if from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                return (value * 9/5) + 32
            elif to_unit == "Kelvin":
                return value + 273.15
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                return (value - 32) * 5/9
            elif to_unit == "Kelvin":
                return (value -32) * 5/9 + 273.15
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                return value - 273.15
            elif to_unit == "Fahrenheit":
                return (value - 273.15) * 9/5 + 32
        return value
    
    if st.button("Convert"):
        result = temperature_conversion(input_value, from_unit, to_unit)
        st.success(f"{input_value:.2f}  {from_unit} is equal to {result:.2f}  {to_unit}") #Like 1 Celsius is equal to 33.8 Fahrenheit.

# Time conversion.
elif category == "Time":
    st.markdown("##### Time Conversion")
    input_value = st.number_input("Enter the Value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From Unit:", ["Seconds", "Minutes", "Hours", "Days", "Weeks", "Months", "Years"])
    to_unit = st.selectbox("To Unit:", ["Seconds", "Minutes", "Hours", "Days", "Weeks", "Months", "Years"])

    # Time Conversion Factors.
    time_conversion = {
        "Seconds": 1, #Base Unit
        "Minutes": 60, #1 Minute is equal to 60 Seconds
        "Hours": 3600, #1 Hour is equal to 3600 Seconds
        "Days": 86400, #1 Day is equal to 86400 Seconds
        "Weeks": 604800, #1 Week is equal to 604800 Seconds
        "Months": 2628000, #1 Month is equal to 2628000 Seconds
        "Years": 31536000, #1 Year is equal to 31536000 Seconds
    }

    # Time Conversion Logic.
    if st.button("Convert"):
        result = input_value * (time_conversion[from_unit] / time_conversion[to_unit])
        st.success(f"{input_value}  {from_unit} is equal to {result:.2f}  {to_unit}")

# Area conversion.
elif category == "Area":
    st.markdown("##### Area Conversion")
    input_value = st.number_input("Enter the Value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From Unit:", ["Square Meters", "Square Kilometers", "Square Feet", "Square Inches", "Square Centimeters", "Square Yards", "Square Miles"])
    to_unit = st.selectbox("To Unit:", ["Square Meters", "Square Kilometers", "Square Feet", "Square Inches", "Square Centimeters", "Square Yards", "Square Miles"])

    # Area Conversion Factors.
    area_conversion = {
        "Square Meters": 1, #Base Unit
        "Square Kilometers": 1000000, #1 Square Kilometer is equal to 1000000 Square Meters
        "Square Feet": 0.092903, #1 Square Foot is equal to 0.092903 Square Meters
        "Square Inches": 0.00064516, #1 Square Inch is equal to 0.00064516 Square Meters
        "Square Centimeters": 0.0001, #1 Square Centimeter is equal to 0.0001 Square Meters
        "Square Yards": 0.836127, #1 Square Yard is equal to 0.836127 Square Meters
        "Square Miles": 2589988.11, #1 Square Mile is equal to 2589988.11 Square Meters
    }

    # Area Conversion Logic.
    if st.button("Convert"):
        result = input_value * (area_conversion[from_unit] / area_conversion[to_unit])
        st.success(f"{input_value}  {from_unit} is equal to {result:.2f}  {to_unit}") #Like 1 Square Kilometer is equal to 1000000 Square Meters.
