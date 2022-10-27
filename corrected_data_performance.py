import pandas as pd
import streamlit as st

cols = [1,2,3]

arr1 = pd.read_excel('chauk_annual cycle comparison.xlsx',usecols=cols)
arr2 = pd.read_excel('hkamti_annual cycle comparison.xlsx', usecols=cols)
arr3 = pd.read_excel('kalewa_annual cycle comparison.xlsx', usecols=cols)
arr4 = pd.read_excel('pyay_annual cycle comparison.xlsx', usecols=cols)

st.title('Monthly Mean Rainfall Cycle Comparison of Regions in Myanmar from 1997 to 2098')
st.write('Observed Period: 1997-2021')
st.write('Projection Period1: 2024-2050')
st.write('Projection Period2: 2049-2075')
st.write('Projection Period3: 2074-2098')

tab1, tab2, tab3, tab4 = st.tabs(["Chauk", "Hkamti", "Kalewa","Pyay"])

with tab1:
   st.header('Data Comparison Using Quantile Mapping Bias-correction Method for Chauk')
   st.line_chart(arr1)

with tab2:
   st.header('Data Comparison Using Quantile Mapping Bias-correction Method for Hkamti')  
   st.line_chart(arr2)

with tab3:
   st.header('Data Comparison Using Quantile Mapping Bias-correction Method for Kalewa')
   st.line_chart(arr3)
   
with tab4:
   st.header('Data Comparison Using Quantile Mapping Bias-correction Method for Pyay')
   st.line_chart(arr4)
