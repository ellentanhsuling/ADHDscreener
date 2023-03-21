import streamlit as st
from utils import columns 

import numpy as np
import pandas as pd
import joblib

#Always use this command to run streamlit: py -m streamlit run predapp.py

model = joblib.load('xgbpipe.joblib')
st.title('ADHD screening')
st.text('Select 1 for Not at all, 2 for Just a Little, 3 for Quite A Bit, 4 for Very Much')
ADHD1  = st.slider("Often fails to give close attention to details or makes careless mistakes in schoolwork, work, or other activities", 1,4, key = 'a')
ADHD2  = st.slider("Often has difficulty sustaining attention in tasks or play activities", 1,4, key = 'b')
ADHD3  = st.slider("Often does not seem to listen when spoken to directly", 1,4, key = 'c')
ADHD4  = st.slider("Often does not follow through on instructions and fails to finish schoolwork, chores, or duties", 1,4, key = 'd')
ADHD5  = st.slider("Often has difficulty organizing tasks and activities", 1,4, key = 'e')
ADHD6  = st.slider("Often avoids, dislikes, or is reluctant to engage in tasks that require sustained mental effort(e.g., schoolwork or homework)", 1,4, key = 'f')
ADHD7  = st.slider("Often loses things necessary for tasks or activities (e.g., toys, school assignments, pencils,books, or tools)", 1,4, key = 'g')
ADHD8  = st.slider("Often is distracted by extraneous stimuli", 1,4, key = 'h')
ADHD9  = st.slider("Often is forgetful in daily activities", 1,4, key = 'i')


def predict(): 
    row = np.array([ADHD1,ADHD2,ADHD3,ADHD4,ADHD5,ADHD6,ADHD7,ADHD8,ADHD9]) 
    X = pd.DataFrame([row], columns = columns)
    prediction = model.predict(X)
    if prediction[0] == 1: 
        st.success('Student scores high for assistance')
    else: 
        st.error('Student is low risk') 

trigger = st.button('Predict', on_click=predict)