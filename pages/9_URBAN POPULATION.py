import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st


url = "https://raw.githubusercontent.com/lethanhdatphumy/Data-Analysis-/ed49225f84d63a1424220cb95f01dea4448166d2/GOD'sDATA.csv"

df = pd.read_csv(url)
df.columns = df.columns.str.strip()


st.sidebar.header('User Input Parameters')


default_countries = data['Country'].unique().tolist()
selected_countries = st.sidebar.multiselect('Country', default_countries, default=default_countries)


default_years = data['Year'].unique().tolist()
selected_years = st.sidebar.multiselect('Year', default_years, default=[1990, 2000, 2010, 2020])


filtered_data = data[data['Country'].isin(selected_countries) & data['Year'].isin(selected_years)]


grouped_data = filtered_data.groupby(['Country', 'Year'])['Urban_population'].sum().unstack()


colors = ["#ff3030", "#F1C40F", "#2980B9", "#D35400"] * len(selected_countries)


plt.figure(figsize=(12, 8))
grouped_data.plot(kind='bar', grid=True, color=colors, width=0.5)


plt.title("Total urban population in Selected Countries\nData Source: World Bank", fontweight='bold', color='#FF5733', fontsize=22)
plt.xlabel("Year", fontsize=16, color='#00AA00', fontweight='bold')
plt.ylabel("Urban Population (Million People)", fontsize=16, color='#00AA00', fontweight='bold')
plt.xticks(fontsize=12, rotation=45)
plt.yticks(fontsize=12)


plt.legend(loc='upper right')


st.pyplot(plt)
