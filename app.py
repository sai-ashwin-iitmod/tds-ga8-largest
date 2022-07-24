import streamlit as st
st.title('Greatest of 3 numbers')
a = st.number_input('Enter number 1')
b = st.number_input('Enter number 2')
c = st.number_input('Enter number 3')
if (a >= b) and (a >= c):
   largest = a
elif (b >= a) and (b >= c):
   largest = b
else:
   largest = c
st.write("Largest of ", a,",", b ,",",c, ",", '= ', largest)
