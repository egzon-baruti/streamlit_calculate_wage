import streamlit as st

from my_functions import calculate_wage

name = st.text_input('Please eneter your name: ')
hour = st.number_input('Please write hours: ' )
rate = st.number_input('Please write rate: ')



if st.button('Calculate the wage!'):
    wage = calculate_wage(hour,rate)
    st.write(f'The total wage for {name} is {wage}')

