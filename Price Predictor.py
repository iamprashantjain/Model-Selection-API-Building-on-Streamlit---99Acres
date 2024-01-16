import pandas as pd
import numpy as np
import streamlit as st
import pickle

st.set_page_config(page_title="Houses Price Predictor")

with open('df.pkl', 'rb') as file:
    df = pickle.load(file)


with open('pipeline.pkl', 'rb') as file:
    pipeline = pickle.load(file)



st.header("Provide your Inputs..")

# st.dataframe(df)

property_type = st.selectbox('Property Type', sorted(df['property_type'].unique().tolist()))
sector = st.selectbox('Sector/Area', sorted(df['sector'].unique().tolist()))
bedRoom = float(st.selectbox('No. Of Bed Rooms', sorted(df['bedRoom'].unique().tolist())))
bathroom = float(st.selectbox('No. Of Bath Rooms', sorted(df['bathroom'].unique().tolist())))
balcony = str(st.selectbox('No. Of Balconies', sorted(df['balcony'].unique().tolist())))
agePossession = str(st.selectbox('Age of Property', sorted(df['agePossession'].unique().tolist())))
built_up_area = float(st.number_input("Built Up Area(In Sqft)"))

user_input1 = st.selectbox("Servant Room", ['Yes', 'No'])
servant_room = 1 if user_input1 == "Yes" else 0

user_input2 = st.selectbox("Store Room", ['Yes', 'No'])
store_room = 1 if user_input2 == "Yes" else 0

furnishing_type = str(st.selectbox('Furnished Type', sorted(df['furnishing_type'].unique().tolist())))
luxury_category = str(st.selectbox('Luxury Rating', sorted(df['luxury_category'].unique().tolist())))
floor_category = str(st.selectbox('Floor', sorted(df['floor_category'].unique().tolist())))

if st.button("Know Price"):
    # Form a DataFrame
    # Predict
    # Display
    data = [[property_type, sector, bedRoom, bathroom, balcony, agePossession, built_up_area, servant_room, store_room,
             furnishing_type, luxury_category, floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony', 'agePossession', 'built_up_area',
               'servant room', 'store room', 'furnishing_type', 'luxury_category', 'floor_category']

    # Convert to DataFrame
    one_df = pd.DataFrame(data, columns=columns)
    # st.dataframe(one_df)
    
    try:
	    predicted_price = np.expm1(pipeline.predict(one_df))[0]

	    low = round((predicted_price - 0.22),2)
	    high = round((predicted_price + 0.22),2)
	    
	    st.header(f"Between {low} Cr. to {high} Cr. Approximately..")

    
    except Exception as e:
    	st.text("Price Not Available..")
    	print(e)