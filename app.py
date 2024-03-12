import requests
import streamlit as st
st.title("Applicationde Prévision Méteo")
city = st.text_input("Entrer le nom d'une ville : ")
api_key = '8e4daf7cddd52c13aa9b45429d0ed1a0'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
print(url)
response = requests.get(url).json()
button = st.button("Afficher la météo")
if button: 
    st.write("Température: ", response['wind'])
