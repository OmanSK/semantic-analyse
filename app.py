import streamlit as st
from model import SemanticModel
from answers import Answer

MODEL = SemanticModel()
ANSWER = Answer()

st.title('Semantic Analysis')
st.write('This application will help you to determine if review'
        'is positive or negative, and its estimated rating')

text = st.text_area('Enter your text')
button = st.button('Analysing ')
spinner = st.spinner(text="In progress...")

if button is True:
    with spinner:
        machine_answer = MODEL.get_result(text)
        semantic, rating = ANSWER.get_result(machine_answer)

    if semantic is not None and rating is not None:
        st.success('Text was successfully analised', icon="✅")
        st.write(f'Semantic is {semantic}')
        st.write(f'Rating is {rating}')
    else:
        st.error('Something went wrong. Try again later', icon="❌")

