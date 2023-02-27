import streamlit as st

st.title("Hi my self Vamshi prakash")
st.snow()

btn_click = st.button("Click Me!")

if btn_click == True:
    st.subheader("You clicked me :cry:")
    st.balloons()