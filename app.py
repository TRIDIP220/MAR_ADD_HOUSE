import streamlit as st
import numpy as np
import joblib
import warnings
warnings.filterwarnings('ignore')

#uploading the model

model= joblib.load("Random_Search (6).pkl")

#Setting the title
st.title("House Price Prediction")

st.markdown("---")

bedroom = st.number_input("Enter the number of Bedroom",min_value=0,value=0)

bathroom = st.number_input("Enter the number of Bathroom",min_value=0,value=0)

Living_area= st.number_input("Living Area",min_value=0,value=2000)

condition= st.number_input("Condition of house",min_value=0,value=3)

school= st.number_input("School No",min_value=0,value=0)

st.markdown("---")

x=[[bedroom,bathroom,Living_area,condition,school]]

pred=st.button("Prediction")


if pred == True:
    np_array= np.array(x)
    price = int(model.predict(np_array)[0])
    st.write(f"House Price {price}")

else:
     st.write("Please click on the prediction button")

