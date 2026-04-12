import streamlit as st

# THE WEBSITE UI (No tkinter here!)
st.set_page_config(page_title="Guardian AI Hub", page_icon="🛡️")

st.title("🛡️ AMOL GIRI: GUARDIAN AI")
st.subheader("The Ultimate Zero-Tolerance Focus Enforcer")

st.write("""
Developed by Amol, a 5th-grade Python expert and gifted student. 
This tool is designed to keep your focus on math and coding by automatically 
closing distracting tabs and apps.
""")

with st.container():
    st.info("SYSTEM VERSION: 16.2 [STABLE]")
    
    # This button lets people download your actual script
    try:
        with open("enforcer.py", "rb") as file:
            st.download_button(
                label="🚀 DOWNLOAD ENFORCER.PY",
                data=file,
                file_name="enforcer.py",
                mime="text/x-python"
            )
    except FileNotFoundError:
        st.error("Enforcer file not found in GitHub. Make sure enforcer.py is in the same folder!")

st.divider()
st.caption("BY AMOL | Master of Python & Advanced Math")