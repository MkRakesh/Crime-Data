# ... (previous code)

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

# ... (rest of the code)

# Create dropdowns for each feature
# ... (previous code)

# Numeric input for Victims_Injured and Victims_Deceased
# ... (previous code)

# Check if Victims_Injured and Victims_Deceased are provided
# ... (previous code)

# Add a Button for Prediction:
if st.button("Predict"):
    # Perform predictions using your model or algorithm
    logmodel = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', LogisticRegression())
    ])

    prediction = loaded_model.predict(toPredict)

    # Determine the prediction result
    if prediction:
        pred = 'Major Attack'
    else:
        pred = 'Minor Attack'

    # Display the prediction result
    st.write("Prediction:", pred)
