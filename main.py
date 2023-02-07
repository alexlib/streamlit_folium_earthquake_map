import streamlit as st
import folium
import pandas as pd
from streamlit_folium import st_folium

def plot_map(data):
    m = folium.Map(location=[35.8, 38.6], zoom_start=6)
    
    for i in range(0, len(data)):
        lat = data.iloc[i]['latitude']
        lon = data.iloc[i]['longitude']
        magnitude = data.iloc[i]['mag']
        folium.Marker([lat, lon], popup=str(magnitude)).add_to(m)
        
    return m

def main():
    st.title("Recent Earthquakes in Turkey and Syria")
    data = pd.read_csv("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.csv")
    st.write(data.head())
    map = plot_map(data)
    # st.write(map)
    st_folium(map, width=725)

if __name__ == "__main__":
    main()
