#!/usr/bin/env python
# coding: utf-8

# In[6]:


import streamlit as st
import joblib
import pandas as pd
from sklearn .preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline


background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://echo.snu.edu/wp-content/uploads/2015/12/Screenshot_2015-11-30-23-12-40-e1449105288676.png");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)
st.text('Deployed on 27/02/2024 by Iftekar Patel @ExcelR')

preprocessor = joblib.load('preprocessor.joblib')
loaded_model = joblib.load('logModel.joblib')





st.title('Terror Attack Prediction')

attack_type_options = ["Bombing","Kidnapping", "Shooting", "Hijacking", "Arson", "Assasination"]


perpetrator_options = ['Group A', 'Group B', 'Group C', 'Group D', 'Group E', 'Group F', 'Group G',
                       'Group H', 'Group I', 'Group J', 'Group K', 'Group L', 'Group M', 'Group N', 
                       'Group O', 'Group P', 'Group Q', 'Group R', 'Group S', 'Group T', 'Group U', 
                       'Group V', 'Group W', 'Group X', 'Group Y', 'Group Z']

weapon_used_options= ["Explosives","Bladed Weapons" ,"Firearms", "Chemicals","Meele"]

claimed_by_options = ['Group A', 'Group B', 'Group C', 'Group D', 'Group E', 'Group F', 'Group G',
                      'Group H', 'Group I', 'Group J', 'Group K', 'Group L', 'Group M', 'Group N',
                      'Group O', 'Group P', 'Group Q', 'Group R', 'Group S', 'Group T', 'Group U', 
                      'Group V', 'Group W', 'Group X', 'Group Y', 'Group Z']




# Create dropdowns for each feature
input1 = st.selectbox("Attack_Type:", attack_type_options)
input3 = st.selectbox("Perpetrator:", perpetrator_options)
input4 = st.selectbox("Weapon_Used:", weapon_used_options)
input5 = st.selectbox("Claimed_by:", claimed_by_options)

# Numeric input for Victims_Injured and Victims_Deceased
input6 = st.number_input("Victims_Injured:", min_value=0)
input7 = st.number_input("Victims_Deceased:", min_value=0)





# Check if Victims_Injured and Victims_Deceased are provided
if input6 > 0 or input7 > 0:
    toPredict = pd.DataFrame({'Attack_Type':[input1], 'Perpetrator':[input3],'Weapon_Used':[input4],'Claimed_By':[input5], 'Victims_Injured':[input6],'Victims_Deceased':[input7]})
    # Create a TensorFlow constant with the input data

    # Add a Button for Prediction:
    if st.button("Predict"):
        # Perform predictions using your model or algorithm
        logmodel = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression( ))
    ])

        prediction = loaded_model.predict(toPredict)

        # Determine the prediction result
        if prediction :
            pred = 'Major Attack'
        else:
            pred = 'Minor Attack'

        # Display the prediction result
        st.write("Prediction:", pred)


# In[ ]:
