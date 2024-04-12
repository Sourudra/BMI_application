import streamlit as st

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi
#Made by Sourudra
#I have got the BMI Scale from https://www.calculator.net/bmi-calculator.html

def get_bmi_category(bmi):
    if bmi < 16:
        return 'Severe Thinness'
    elif bmi < 17:
        return 'Moderate Thinness'
    elif bmi < 18.5:
        return 'Mild Thinness'
    elif bmi < 25:
        return 'Normal'
    elif bmi < 30:
        return 'Overweight'
    elif bmi < 35:
        return 'Obese Class I'
    elif bmi < 40:
        return 'Obese Class II'
    else:
        return 'Obese Class III'

def convert_height_to_meters(feet, inches):
    total_inches = feet * 12 + inches
    height_meters = total_inches * 0.0254  # Convert inches to meters
    return height_meters

st.title('BMI Calculator')

# Input fields for weight, height, and gender
weight = st.number_input('Enter your weight (kg)', min_value=1.0)
height_unit = st.radio('Select height unit', ('cm', 'ft/in'))
if height_unit == 'cm':
    height = st.number_input('Enter your height (cm)', min_value=1.0)
else:
    feet = st.number_input('Feet', min_value=1)
    inches = st.number_input('Inches', min_value=0, max_value=11)
    height = convert_height_to_meters(feet, inches)

# Calculate BMI and BMI category
if st.button('Calculate BMI'):
    if weight <= 0 or height <= 0:
        st.error('Please enter valid weight and height values.')
    else:
        bmi = calculate_bmi(weight, height)
        bmi_category = get_bmi_category(bmi)
        st.write(f'Your BMI: {bmi:.2f}')
        st.write(f'BMI Category: {bmi_category}')
