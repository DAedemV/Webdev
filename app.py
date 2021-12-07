import streamlit as st

left_block, center_block, right_block = st.columns([2, 2, 2])

with left_block:
    st.write('# LEFT BLOCK')
    first_container = st. container()
    with first_container:
        st.header('Mon premier container')

with center_block:
    st.write('# CENTER BLOCK')

with right_block:
    st.write('# RIGHT BLOCK')






