import requests
import streamlit as st
import pickle
import numpy as np

model=pickle.load(open("model.pkl","rb"))

API_KEY="58f79ab851bc6054d989a4f6eedbfce4"
def get_temperature(city):
    url= f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    resp=requests.get(url)
    dataa=resp.json()
    st.write(dataa)

    if dataa.get("cod")!=200:
        return None,None,None
    
    humidityy=dataa['main']['humidity']
    pressuree=dataa['main']['pressure']
    wind_speed=dataa['wind']['speed']

    return humidityy,pressuree,wind_speed

city=st.text_input("Enter City Name")
if st.button("Predict Temperature"):

    if city=="":
        st.warning("Enter city name")

    else:
        humidityy,pressuree,wind_speed=get_temperature(city)

    if humidityy is None:
        st.error("City not found or API issue")

    else:
        dataa=np.array([[humidityy,wind_speed,pressuree,4,15]])
        resultt=model.predict(dataa)

        st.success(f"Predicted Temperature: {resultt[0]:.2f} °C")
