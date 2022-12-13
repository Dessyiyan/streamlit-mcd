import pickle 
import numpy as np
import streamlit as st

model = pickle.load(open('category_mcd.sav', 'rb'))

st.title('prediksi kategori menu mcdonald')

col1, col2, col3 = st.columns(3)

with col1 :
	Calories = st.number_input('input kalori')

	Calories_from_Fat = st.number_input('input calories from fat')

	Total_Fat = st.number_input('input total fat')

	Total_FatDailyValue = st.number_input('input jumlah saudara')

	Saturated_Fat = st.number_input('input jumlah Saturated_Fat')

	Saturated_FatDailyValue = st.number_input('input jumlah Saturated_FatDailyValue')

	Trans_Fat = st.number_input('input jumlah Trans_Fat')

	Cholesterol = st.number_input('input jumlah Cholesterol')

with col2:	

	CholesterolDailyValue = st.number_input('input CholesterolailyValue')

	Sodium = st.number_input('input Sodium')

	SodiumDailyValue = st.number_input('input total SodiumDailyValue')

	Total_FatDailyValue = st.number_input('input jumlah Total_FatDailyValue')

	Carbohydrates = st.number_input('input jumlah Carbohydrates')

	CarbohydratesDailyValue = st.number_input('input jumlah CarbohydratesDailyValue')

	Dietary_Fiber = st.number_input('input jumlah Dietary_Fiber')

	Dietary_FiberDailyValue = st.number_input('input Dietary_FiberDailyValue')

with col3:

	Sugars = st.number_input('input Sugars')

	Protein = st.number_input('input Protein')

	Vitamin_ADailyValue  = st.number_input('input Vitamin_ADailyValue')

	Vitamin_CDailyValue = st.number_input('input jumlah Vitamin_CDailyValue')

	CalciumDailyValue = st.number_input('input jumlah CalciumDailyValue')

	IronDailyValue = st.number_input('input IronDailyValue')

prediksi = ''

if st.button('prediksi kategori'):
	category_prediksi = model.predict([[Calories,Calories_from_Fat,Total_Fat,Total_FatDailyValue,Saturated_Fat,Saturated_FatDailyValue,Trans_Fat,Cholesterol,CholesterolDailyValue,Sodium,SodiumDailyValue,Carbohydrates,CarbohydratesDailyValue,Dietary_Fiber,Dietary_FiberDailyValue,Sugars,Protein,Vitamin_ADailyValue,Vitamin_CDailyValue,CalciumDailyValue,IronDailyValue]])

	if(category_prediksi[0]==1):
		prediksi = 'coffee and tea'
	elif(category_prediksi[0]==2):
		prediksi = 'breakfast'
	elif(category_prediksi[0]==3):
		prediksi = 'smoothies  & shakes'
	elif(category_prediksi[0]==4):
		prediksi = 'beverages'
	elif(category_prediksi[0]==5):
		prediksi = 'chicken & fish'
	elif(category_prediksi[0]==6):
		prediksi = 'beef & pork'
	elif(category_prediksi[0]==7):
		prediksi = 'snack & sides'
	elif(category_prediksi[0]==8):
		prediksi = 'desserts'
	elif(category_prediksi[0]==9):
		prediksi = 'salads'
	else :
		prediksi = 'kategori salah'


st.success(prediksi)