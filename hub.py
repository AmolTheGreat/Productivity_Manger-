import streamlit as st

st.set_page_config(page_title="Guardian AI Hub", page_icon="🛡️")

st.title("🛡️ AMOL GIRI: GUARDIAN AI")
st.write("Stay focused. Stay coding.")

# Since 'enforcer.pyw' is at Index 0 in your main folder:
try:
    with open("enforcer.pyw", "rb") as file:
        st.download_button(
            label="🚀 DOWNLOAD & LAUNCH GUARDIAN AI",
            data=file,
            file_name="GuardianAI.pyw",
            mime="text/x-python"
        )
    st.success("✅ SYSTEM READY: Guardian AI is live!")
except FileNotFoundError:
    st.error("Wait, the server just saw it... where did it go? Refresh the page!")

st.divider()
st.caption("Developed by Amol | WAVE Magnet Program")