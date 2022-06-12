# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 08:24:00 2022
@author: MuhammadAli
@org: Deep Learning Lab
@hackathon: Swiss AI
"""

from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd

#with st.echo(code_location='below'):
def predict_rating(model, df):
    
    predictions_data = predict_model(estimator = model, data = df)
    
    return predictions_data[['Label', 'Score']]
    
model = load_model('model/random_forest_v1')

st.title('Illicit Transaction Classification Web App')
st.write('This is a web app to classify whether a Bitcoin transaction is legal or not based on\
        several features provided by Elliptic Ltd. is a London-based blockchain analysis provider. Please upload the\
        csv file with a transaction record that you want to test. After that, click on the Predict button at the bottom to\
        see the prediction.')

# file(s) part
features_df=None
uploaded_file = st.file_uploader("Upload your CSV file")
if uploaded_file is not None:
  features_df = pd.read_csv(uploaded_file)

if st.button('Predict'):
    if dataframe is None:
        st.error("Please Upload Your CSV")
    else:
        with st.spinner('File is Processing...'):
          output = predict_rating(model, features_df)
          csv = convert_df(output)
          st.download_button(label="Download Generated Output CSV", file_name='output_data.csv', data=csv, mime='text/csv')
          st.success('And your file is ready!')
