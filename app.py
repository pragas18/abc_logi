
import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load the model
# Assuming 'logi.sav' is in the same directory as this app.py or in /content/
try:
    model = joblib.load('logi.sav')
except FileNotFoundError:
    st.error("Error: 'logi.sav' model file not found. Please ensure it's in the same directory as app.py or in /content/.")
    st.stop()

st.title('Delivery Delay Prediction App')
st.write('Enter the details below to predict if there will be a delivery delay.')

# Define the features based on X.columns from the notebook
feature_names = [
    'Delivery_Distance', 'Traffic_Congestion', 'Weather_Condition', 'Delivery_Slot',
    'Driver_Experience', 'Num_Stops', 'Vehicle_Age', 'Road_Condition_Score',
    'Package_Weight', 'Fuel_Efficiency', 'Warehouse_Processing_Time'
]

# Create input fields for each feature
input_data = {}
for feature in feature_names:
    # Using st.number_input for numerical inputs. 
    # You might want to adjust min_value, max_value, and step for more realistic ranges
    # For simplicity, I'm using generic values for now.
    if feature == 'Delivery_Distance':
        input_data[feature] = st.number_input(f'{feature} (e.g., 10.5)', value=20.0, step=0.1)
    elif feature == 'Traffic_Congestion':
        input_data[feature] = st.slider(f'{feature} (1-5, 5 being high)', min_value=1, max_value=5, value=3)
    elif feature == 'Weather_Condition':
        input_data[feature] = st.slider(f'{feature} (1-3, 3 being severe)', min_value=1, max_value=3, value=2)
    elif feature == 'Delivery_Slot':
        input_data[feature] = st.slider(f'{feature} (1-3)', min_value=1, max_value=3, value=2)
    elif feature == 'Driver_Experience':
        input_data[feature] = st.number_input(f'{feature} (years)', min_value=0, value=5, step=1)
    elif feature == 'Num_Stops':
        input_data[feature] = st.number_input(f'{feature}', min_value=0, value=3, step=1)
    elif feature == 'Vehicle_Age':
        input_data[feature] = st.number_input(f'{feature} (years)', min_value=0, value=5, step=1)
    elif feature == 'Road_Condition_Score':
        input_data[feature] = st.slider(f'{feature} (1-5, 5 being excellent)', min_value=1, max_value=5, value=3)
    elif feature == 'Package_Weight':
        input_data[feature] = st.number_input(f'{feature} (kg)', value=10.0, step=0.1)
    elif feature == 'Fuel_Efficiency':
        input_data[feature] = st.number_input(f'{feature} (km/L)', value=15.0, step=0.1)
    elif feature == 'Warehouse_Processing_Time':
        input_data[feature] = st.number_input(f'{feature} (minutes)', value=60, step=1)


if st.button('Predict Delivery Delay'):
    # Convert input data to a numpy array or DataFrame as expected by the model
    features = pd.DataFrame([input_data])
    
    # Make prediction
    prediction = model.predict(features)[0]
    prediction_proba = model.predict_proba(features)[0]

    st.subheader('Prediction Results:')
    if prediction == 1:
        st.error('There is a predicted **DELIVERY DELAY** ⚠️')
    else:
        st.success('No predicted delivery delay. Looks good! ✅')
    
    st.write(f"Probability of No Delay: {prediction_proba[0]*100:.2f}%")
    st.write(f"Probability of Delay: {prediction_proba[1]*100:.2f}%")

