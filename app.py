import streamlit as st

st.title("Innomatics Data App")
st.spinner()

btn_click = st.button("Click Me!")

if btn_click == True:
    st.subheader("You clicked me :smile:")
    st.balloons()
