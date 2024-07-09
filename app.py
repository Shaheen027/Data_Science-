'''
Created on 29/06/2024
@author: Shaheen Khatoon
'''
import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set Page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# Getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# Loading the saved model
model_path = os.path.join(working_dir, 'C:/Users/DEll/Desktop/breast cancer prediction/bcp.pkl')
with open(model_path, 'rb') as file:
    breast_cancer_model = pickle.load(file)

# Side bar for navigation
with st.sidebar:
    selected = option_menu('Main Menu', ['Breast Cancer Prediction'],
                           menu_icon='hospital-fill',
                           default_index=0)

# Breast cancer prediction page
if selected == 'Breast Cancer Prediction':
    # Page title
    st.title('Breast Cancer Prediction')
    
    # Input fields
    col1, col2, col3 = st.columns(3)
   
    with col1:
        radius_mean = st.text_input('Radius Mean')
    with col2:
        texture_mean = st.text_input('Texture Mean')
    with col3:
        perimeter_mean = st.text_input('Perimeter Mean')
    with col1:
        area_mean=st.text_input('Area Mean')
    with col2:
        smoothness_mean = st.text_input('Smoothness Mean')
    with col3:
        compactness_mean = st.text_input('Compactness Mean')
    with col1:
        concavity_mean = st.text_input('Concavity Mean')
    with col2:
        concave_points_mean = st.text_input('Concave Points Mean')
    with col3:
        symmetry_mean = st.text_input('Symmetry Mean')
    with col1:
        fractal_dimension_mean = st.text_input('Fractal Dimension Mean')
    
    with col2:
        radius_se = st.text_input('Radius se')
    with col3:
        texture_se = st.text_input('Texture se')
    with col1:
        perimeter_se= st.text_input('Perimeter se')
    with col2:
        area_se=st.text_input('Area se')
    with col3:
        smoothness_se = st.text_input('Smoothness se')
    with col1:
        compactness_se = st.text_input('Compactness se')
    with col2:
        concavity_se = st.text_input('Concavity se')
    with col3:
        concave_points_se = st.text_input('Concave Points se')
    with col1:
        symmetry_se = st.text_input('Symmetry se')
    with col2:
        fractal_dimension_se = st.text_input('Fractal Dimension se')
    
    
    
    with col3:
        radius_worst = st.text_input('Radius worst')
    with col1:
        texture_worst = st.text_input('Texture worst')
    with col2:
        perimeter_worst= st.text_input('Perimeter worst')
    with col3:
        area_worst=st.text_input('Area worst')
    with col1:
        smoothness_worst = st.text_input('Smoothness worst')
    with col2:
        compactness_worst= st.text_input('Compactness worst')
    with col3:
        concavity_worst = st.text_input('Concavity worst')
    with col1:
        concave_points_worst = st.text_input('Concave Points worst')
    with col2:
        symmetry_worst = st.text_input('Symmetry worst')
    with col3:
        fractal_dimension_worst = st.text_input('Fractal Dimension worst')



    # Code for prediction
    breast_cancer_diagnosis = ''

    # Creating a button for prediction
    if st.button('Predict'):
        try:
            user_input = [ float(radius_mean), float(texture_mean), float(perimeter_mean),float(area_mean),
                          float(smoothness_mean), float(compactness_mean), float(concavity_mean), 
                          float(concave_points_mean), float(symmetry_mean), float(fractal_dimension_mean), float(radius_se), float(texture_se), float(perimeter_se),float(area_se),
                          float(smoothness_se), float(compactness_se), float(concavity_se), 
                          float(concave_points_se), float(symmetry_se), float(fractal_dimension_se),float(radius_worst), float(texture_worst), float(perimeter_worst),float(area_worst),
                          float(smoothness_worst), float(compactness_worst), float(concavity_worst), 
                          float(concave_points_worst), float(symmetry_worst), float(fractal_dimension_worst)]
            
            prediction = breast_cancer_model.predict([user_input])
            
            if prediction[0] == 1:
                breast_cancer_diagnosis = 'The person is having breast cancer'
            else:
                breast_cancer_diagnosis = 'The person is not having breast cancer'

            st.success(breast_cancer_diagnosis)
        except Exception as e:
            st.error(f"Error in prediction: {e}")
