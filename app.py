import streamlit as st

st.set_page_config(
    page_title="Ram AI Assistant",
    page_icon="🤖"
)

st.title("🤖 Ram AI Assistant")

st.write("Hi! What do you want to learn today?")
st.write("హలో! ఈరోజు ఏమి నేర్చుకోవాలనుకుంటున్నారు?")

question = st.text_input("Ask Ram / రామ్‌ను అడుగు")

if question:
    st.write("Your question:", question)
    st.info("AI service is not connected yet.")